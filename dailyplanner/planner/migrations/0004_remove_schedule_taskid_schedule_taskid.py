# Generated by Django 5.0 on 2023-12-25 16:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("planner", "0003_userprofile_maxxp"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="schedule",
            name="taskID",
        ),
        migrations.AddField(
            model_name="schedule",
            name="taskID",
            field=models.ManyToManyField(to="planner.task"),
        ),
    ]