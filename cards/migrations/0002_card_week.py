# Generated by Django 4.2.7 on 2023-11-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="card",
            name="week",
            field=models.IntegerField(null=True),
        ),
    ]
