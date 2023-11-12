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
        ]
        read_only_fields = ["reg_date"]
        extra_kwargs = {
            "writer": {"required": False},
        }
