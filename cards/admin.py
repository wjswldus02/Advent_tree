from django.contrib import admin

from . import models


@admin.register(models.Card)
class CardAdmin(admin.ModelAdmin):
    list_filter = ("week",)

    list_display = [
        "writer",
        "content",
        "reg_date",
        "week",
        "ornament_x",
        "ornament_y",
    ]
