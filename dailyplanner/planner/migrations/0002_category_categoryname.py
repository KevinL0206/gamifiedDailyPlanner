# Generated by Django 5.0 on 2023-12-25 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("planner", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="categoryName",
            field=models.CharField(default=None, max_length=255),
        ),
    ]
