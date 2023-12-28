from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime
from .functions import addXP
# Create your views here.

def displaySchedule(request):
    currentUser = request.user
    userInstance = User.objects.get(username = currentUser)
    scheduleInstance = schedule.objects.get(user = userInstance)
    userProfileInstance = userProfile.objects.get(user = userInstance)

    experience = userProfileInstance.experience
    level = userProfileInstance.level
    maxXP = userProfileInstance.maxXP
    tasks = scheduleInstance.taskID.all()
    task_ids = [task.taskID for task in tasks]
    taskInfos = [task.taskInfo for task in tasks]
    flags = []

    for id in task_ids:
        completedInstance = completed.objects.get(userID = userProfileInstance, taskID = id)
        flags.append(completedInstance.completedFlag)

    taskzip = zip(taskInfos,flags)

    context = {
        'user' : currentUser,
        'tasks' : taskzip,
        'experience' : experience,
        'max' : maxXP,
        'level' : level,
        
        }

    return render(request,'schedule.html',context)
