# Generated by Django 5.0 on 2023-12-26 17:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("planner", "0005_remove_task_completedflag_completed"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="xpMultiplier",
            field=models.IntegerField(default=1),
        ),
    ]
