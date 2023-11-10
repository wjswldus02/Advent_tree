from django.db import models
from django.db import IntegrityError

class Card(models.Model):
    writer = models.CharField(max_length=100)
    reg_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    week = models.IntegerField(default = 0)

