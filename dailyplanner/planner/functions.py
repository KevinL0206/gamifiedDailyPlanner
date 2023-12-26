from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from datetime import datetime
# Create your views here.

@login_required
def dateDiff(request):
    currentUser = request.user
    userInstance = currentUser.userProfile
    lastLogin = userInstance.lastLogin
    currentDate = datetime.datetime.now()
    return int(currentDate - lastLogin)
    
@login_required
def resetSchedule(request):
    currentUser = request.user
    userInstance = currentUser.userProfile
    completedInstance = completed.objects.get(userID = currentUser)
    
    currentDate = datetime.datetime.now()
    lastLogin = userInstance.lastLogin
    currentDay = currentDate.day
    lastLoginDay = lastLogin.day

    if currentDay != lastLoginDay:
        for task in completedInstance:
            completedInstance.completedFlag = False
            completedInstance.save()

@login_required
def addXP(request,task):
    resetSchedule()
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
    
    completedInstance = completed.objects.get(userid=currentUser,taskID = completedTask)
    completedFlag = completedInstance.completedFlag
    xpGain =taskBaseXP * taskXPMultiplier

    if not completedFlag:
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
    else:
        messages.success(request,'Task Has Already Been Completed')







