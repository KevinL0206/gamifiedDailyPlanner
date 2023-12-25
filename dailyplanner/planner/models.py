from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lastLogin = models.DateField(default = timezone.now)
    experience = models.IntegerField(default = 0)
    level = models.IntegerField(default = 0)

class category(models.Model):
    categoryID = models.AutoField(primary_key=True)
    baseXP = models.IntegerField(default = 0)

class task(models.Model):
    taskID = models.AutoField(primary_key=True)
    categoryID = models.ForeignKey(category,on_delete=models.CASCADE)
    completedFlag = models.BooleanField(default = False)
    taskInfo = models.CharField(max_length=255)

class schedule(models.Model):
    scheduleID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    taskID = models.ForeignKey(task,on_delete=models.CASCADE)
    schedule_day = models.DateField(default = timezone.now)