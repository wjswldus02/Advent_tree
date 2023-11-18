from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        # fields = "__all__"
        fields = [
            "id",
            "writer",
            "content",
            "week",
            "ornament_x",
            "ornament_y",
        ]
        read_only_fields = [
            "reg_date",
            "week",
            "ornament_x",
            "ornament_y",
        ]
        extra_kwargs = {
            "writer": {"required": False},
        }
