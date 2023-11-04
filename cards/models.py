from django.db import models


class Card(models.Model):
    writer = models.CharField(max_length=100)
    reg_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
