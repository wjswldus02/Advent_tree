from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.Card)
class CardAdmin(admin.ModelAdmin):
    list_display = [
        "writer",
        "content",
        "reg_date",
    ]