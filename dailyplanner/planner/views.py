from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime
# Create your views here.

def addXP(request,task):
    currentUser = request.user

    userInstance = currentUser.userProfile
    completedTask = task
    currentLevel = userInstance.level
    currentExperience = userInstance.experience
    maximumExperience = userInstance.maxXP

    taskInstance = task.objects.get(taskID = completedTask)
    taskCategory = taskInstance.categoryID
    taskXPMultiplier = taskInstance.xpMultiplier

    categoryInstance = category.objects.get(categoryID = taskCategory)
    taskBaseXP = categoryInstance.baseXP

    xpGain =taskBaseXP * taskXPMultiplier

    if currentExperience + xpGain <= maximumExperience: #Experience gain is not enough to level up
        userInstance = currentUser.userProfile
        userInstance.experience = currentExperience + xpGain
        userInstance.save()
    else:
        userInstance = currentUser.userProfile #Experience gain results in level up
        overflow = (currentExperience + xpGain) - maximumExperience
        userInstance.level = currentLevel + 1
        userInstance.experience = overflow
        userInstance.save()


def dateDiff(request,date):
    currentUser = request.user
    userInstance = currentUser.userProfile
    lastLogin = userInstance.lastLogin
    currentDate = datetime.datetime.now()
    return int(currentDate - lastLogin)
    

def resetSchedule(schedule):
    pass

def getuserTasks(schedule):
    pass

