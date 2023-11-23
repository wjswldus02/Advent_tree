from datetime import datetime

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from . import models, serializers
from config.logger.setup_logger import logger


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = models.Notice.objects.all()
    serializer_class = serializers.NoticeSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        current_date = datetime.now()
        if datetime(2023, 11, 26) <= current_date <= datetime(2023, 12, 2):
            current_week = 1
        elif datetime(2023, 12, 3) <= current_date <= datetime(2023, 12, 9):
            current_week = 2
        elif datetime(2023, 12, 10) <= current_date <= datetime(2023, 12, 16):
            current_week = 3
        elif datetime(2023, 12, 17) <= current_date <= datetime(2023, 12, 23):
            current_week = 4
        else:
            current_week = 0
        if r_week := request.GET.get("week"):
            current_week = r_week

        logger.info(f"{current_week=}")

        # week 값에 따라 필터링
        queryset = self.queryset.filter(week=current_week).order_by("-reg_date").first()
        if queryset:
            serializer = self.get_serializer(queryset)
            return Response({"result": serializer.data})
        else:
            return Response({"result": None})
