from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lastLogin = models.DateField(default = timezone.now)
    level = models.IntegerField(default = 0)
    experience = models.IntegerField(default = 0)
    maxXP = models.IntegerField(default = 50)

    def __str__(self):
        return self.user.username

class category(models.Model):
    categoryID = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length = 255, default=None)
    baseXP = models.IntegerField(default = 0)

    def __str__(self):
        return self.category.categoryName

class task(models.Model):
    taskID = models.AutoField(primary_key=True)
    categoryID = models.ForeignKey(category,on_delete=models.CASCADE)
    completedFlag = models.BooleanField(default = False)
    taskInfo = models.CharField(max_length=255)

    def __str__(self):
        return self.task.taskInfo

class schedule(models.Model):
    scheduleID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    taskID = models.ForeignKey(task,on_delete=models.CASCADE)
    schedule_day = models.DateField(default = timezone.now)

    def __str__(self):
        return self.schedule.user.username