from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from datetime import datetime
# Create your views here.


@login_required
def resetSchedule(request):
    currentUser = request.user
    user_instance = User.objects.get(username=currentUser)         
    profileInstance = userProfile.objects.get(user=user_instance)

    completedInstance = completed.objects.get(userID = currentUser)
    
    currentDate = date.today()
    lastLogin = profileInstance.tempDate
    currentDay = currentDate.day
    lastLoginDay = lastLogin.day

    if currentDay != lastLoginDay:
        for task in completedInstance:
            completedInstance.completedFlag = False
            completedInstance.save()

@login_required
def addXP(request,task):
    resetSchedule()

    #Create Model Instances
    currentUser = request.user

    user_instance = User.objects.get(username=currentUser)         
    profileInstance = userProfile.objects.get(user=user_instance)

    completedTask = task
    currentLevel = profileInstance.level
    currentExperience = profileInstance.experience
    maximumExperience = profileInstance.maxXP

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


    #Check Completion Streaks, Update Multipliers
    
    if lastCompletion != datetime.date(1,1,1):
        dateDiff = date.today() - lastCompletion
        if dateDiff >= 3:
            negMultiplier = 0.75
    
    if completedInstance.streak >= 3:
        posMultiplier = 1.25
    
    xpGain =taskBaseXP * taskXPMultiplier * negMultiplier * posMultiplier
    
    #Update XP if task not completed
    if not completedFlag:
        if currentExperience + xpGain <= maximumExperience: #Experience gain is not enough to level up
            user_instance = User.objects.get(username=currentUser)         
            profileInstance = userProfile.objects.get(user=user_instance)
            profileInstance.experience = currentExperience + xpGain
            profileInstance.save()
            completedInstance.completedFlag = True
            completedInstance.streak += 1
            completedInstance.save()
        else:
            user_instance = User.objects.get(username=currentUser)         
            profileInstance = userProfile.objects.get(user=user_instance) #Experience gain results in level up
            overflow = (currentExperience + xpGain) - maximumExperience
            profileInstance.level = currentLevel + 1
            profileInstance.experience = overflow
            profileInstance.save()
            completedInstance.completedFlag = True
            completedInstance.streak += 1
            completedInstance.save()
    else:
        messages.success(request,'Task Has Already Been Completed')







