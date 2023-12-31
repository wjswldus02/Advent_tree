from datetime import datetime
from zoneinfo import ZoneInfo

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
        current_date = datetime.now(tz=ZoneInfo("Asia/Seoul"))
        if (
            datetime(2023, 12, 3, tzinfo=ZoneInfo("Asia/Seoul"))
            <= current_date
            < datetime(2023, 12, 10, tzinfo=ZoneInfo("Asia/Seoul"))
        ):
            current_week = 1
        elif (
            datetime(2023, 12, 10, tzinfo=ZoneInfo("Asia/Seoul"))
            <= current_date
            < datetime(2023, 12, 17, tzinfo=ZoneInfo("Asia/Seoul"))
        ):
            current_week = 2
        elif (
            datetime(2023, 12, 17, tzinfo=ZoneInfo("Asia/Seoul"))
            <= current_date
            < datetime(2023, 12, 24, tzinfo=ZoneInfo("Asia/Seoul"))
        ):
            current_week = 3
        elif (
            datetime(2023, 12, 24, tzinfo=ZoneInfo("Asia/Seoul"))
            <= current_date
            < datetime(2023, 12, 31, tzinfo=ZoneInfo("Asia/Seoul"))
        ):
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
