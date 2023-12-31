# Generated by Django 5.0 on 2023-12-26 19:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("planner", "0006_task_xpmultiplier"),
    ]

    operations = [
        migrations.AddField(
            model_name="completed",
            name="dateCompleted",
            field=models.DateField(default=datetime.date(1, 1, 1)),
        ),
        migrations.AddField(
            model_name="completed",
            name="streak",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="experience",
            field=models.FloatField(default=0),
        ),
    ]
