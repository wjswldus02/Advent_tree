from datetime import datetime
from zoneinfo import ZoneInfo
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.forms import ValidationError

from config.logger.setup_logger import logger
from utils.utils import generate_point_inside_triangle_with_distance, load_profanity_list


class Card(models.Model):
    img_path = models.CharField(max_length=100, blank=True)
    writer = models.CharField(max_length=100)
    reg_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    week = models.IntegerField(default=0)
    ornament_x = models.CharField(max_length=100, blank=True)
    ornament_y = models.CharField(max_length=100, blank=True)


@receiver(pre_save, sender=Card)
def data_process(sender, instance, **kwargs):
    current_date = datetime.now(tz=ZoneInfo("Asia/Seoul"))
    if (
        datetime(2023, 12, 3, tzinfo=ZoneInfo("Asia/Seoul"))
        <= current_date
        <= datetime(2023, 12, 9, tzinfo=ZoneInfo("Asia/Seoul"))
    ):
        instance.week = 1
    elif (
        datetime(2023, 12, 10, tzinfo=ZoneInfo("Asia/Seoul"))
        <= current_date
        <= datetime(2023, 12, 16, tzinfo=ZoneInfo("Asia/Seoul"))
    ):
        instance.week = 2
    elif (
        datetime(2023, 12, 17, tzinfo=ZoneInfo("Asia/Seoul"))
        <= current_date
        <= datetime(2023, 12, 23, tzinfo=ZoneInfo("Asia/Seoul"))
    ):
        instance.week = 3
    elif (
        datetime(2023, 12, 24, tzinfo=ZoneInfo("Asia/Seoul"))
        <= current_date
        <= datetime(2023, 12, 30, tzinfo=ZoneInfo("Asia/Seoul"))
    ):
        instance.week = 4
    else:
        instance.week = 0

    count = Card.objects.count()
    ornament_coordinates = Card.objects.filter(week=instance.week).values_list("ornament_x", "ornament_y")
    instance.ornament_x, instance.ornament_y = generate_point_inside_triangle_with_distance(
        count,
        1200,
        ornament_coordinates,
    )

    logger.info(f"{vars(instance)}")

    profanity_list = load_profanity_list()
    for profanity in profanity_list:
        if profanity in instance.content:
            logger.warning(f"{instance.content=}")
            raise ValidationError("욕설이 포함되어 있어서 저장이 거부되었습니다.")
