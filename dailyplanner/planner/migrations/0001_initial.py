# Generated by Django 5.0 on 2023-12-25 16:08

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="category",
            fields=[
                ("categoryID", models.AutoField(primary_key=True, serialize=False)),
                ("baseXP", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="task",
            fields=[
                ("taskID", models.AutoField(primary_key=True, serialize=False)),
                ("completedFlag", models.BooleanField(default=False)),
                ("taskInfo", models.CharField(max_length=255)),
                (
                    "categoryID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="planner.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="schedule",
            fields=[
                ("scheduleID", models.AutoField(primary_key=True, serialize=False)),
                ("schedule_day", models.DateField(default=django.utils.timezone.now)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "taskID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="planner.task"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="userProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("lastLogin", models.DateField(default=django.utils.timezone.now)),
                ("experience", models.IntegerField(default=0)),
                ("level", models.IntegerField(default=0)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
