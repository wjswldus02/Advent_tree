# Generated by Django 4.2.7 on 2023-11-18 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0002_card_week"),
    ]

    operations = [
        migrations.AddField(
            model_name="card",
            name="ornament_x",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="card",
            name="ornament_y",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name="card",
            name="week",
            field=models.IntegerField(default=0),
        ),
    ]
