from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.forms import ValidationError


class Card(models.Model):
    writer = models.CharField(max_length=100)
    reg_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    week = models.IntegerField(null=True)


@receiver(pre_save, sender=Card)
def check_for_profanity(sender, instance, **kwargs):
    # 여기서는 단순히 '욕설' 이라는 단어가 포함되어 있는지 확인하였습니다.
    # 실제로는 더 강력한 욕설 필터링 로직을 구현해야 할 것입니다.
    profanity_list = ['18']
    for profanity in profanity_list:
        if profanity in instance.content:
            raise ValidationError("욕설이 포함되어 있어서 저장이 거부되었습니다.")