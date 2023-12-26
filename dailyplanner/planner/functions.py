from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from datetime import datetime
# Create your views here.

@login_required

    
@login_required
def resetSchedule(request):
    currentUser = request.user
    userInstance = currentUser.userProfile
    completedInstance = completed.objects.get(userID = currentUser)
    
    currentDate = datetime.day()
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
    lastCompletion = completedInstance.dateCompleted

    negMultiplier = 1
    posMultiplier = 1

    """
    check last the last date the task was completed, 
    if it has been more than 3 days, reduce xp gain
    """
    if lastCompletion != datetime.date(1,1,1):
        dateDiff = datetime.day() - lastCompletion
        if dateDiff >= 3:
            negMultiplier = 0.75
    
    if completedInstance.streak >= 3:
        posMultiplier = 1.25
    
    xpGain =taskBaseXP * taskXPMultiplier * negMultiplier * posMultiplier
    
    if not completedFlag:
        if currentExperience + xpGain <= maximumExperience: #Experience gain is not enough to level up
            userInstance = currentUser.userProfile
            userInstance.experience = currentExperience + xpGain
            userInstance.save()
            completedInstance.completedFlag = True
            completedInstance.streak += 1
            completedInstance.save()
        else:
            userInstance = currentUser.userProfile #Experience gain results in level up
            overflow = (currentExperience + xpGain) - maximumExperience
            userInstance.level = currentLevel + 1
            userInstance.experience = overflow
            userInstance.save()
            completedInstance.completedFlag = True
            completedInstance.streak += 1
            completedInstance.save()
    else:
        messages.success(request,'Task Has Already Been Completed')







