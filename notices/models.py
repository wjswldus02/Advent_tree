from django.db import models


class Notice(models.Model):
    reg_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True)
    notice = models.TextField()
    week = models.IntegerField(default=0)
