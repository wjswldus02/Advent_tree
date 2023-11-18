from datetime import datetime
from zoneinfo import ZoneInfo
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.forms import ValidationError

from utils.utils import generate_point_inside_triangle_with_distance, load_profanity_list


class Card(models.Model):
    writer = models.CharField(max_length=100)
    reg_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    week = models.IntegerField(default=0)
    ornament_x = models.CharField(max_length=100, blank=True)
    ornament_y = models.CharField(max_length=100, blank=True)


@receiver(pre_save, sender=Card)
def data_process(sender, instance, **kwargs):
    current_date = datetime.now()
    if datetime(2023, 11, 26) <= current_date <= datetime(2023, 12, 2):
        instance.week = 1
    elif datetime(2023, 12, 3) <= current_date <= datetime(2023, 12, 9):
        instance.week = 2
    elif datetime(2023, 12, 10) <= current_date <= datetime(2023, 12, 16):
        instance.week = 3
    else:
        instance.week = 4

    count = Card.objects.count()
    ornament_coordinates = Card.objects.filter(week=instance.week).values_list("ornament_x", "ornament_y")
    print(ornament_coordinates)
    instance.ornament_x, instance.ornament_y = generate_point_inside_triangle_with_distance(
        count,
        2000,
        ornament_coordinates,
    )

    profanity_list = load_profanity_list()
    for profanity in profanity_list:
        if profanity in instance.content:
            raise ValidationError("욕설이 포함되어 있어서 저장이 거부되었습니다.")
