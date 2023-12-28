from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime
from .functions import addXP
from django.contrib import messages
from .forms import addTask,completeTask

# Create your views here.

def displaySchedule(request):
    currentUser = request.user
    completedTaskForm = completeTask()

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
        'form' : completedTaskForm,
        
        }
    
    if request.method == "POST":
        form = completeTask(request.POST)

        if form.is_valid():
            taskInfo = form.cleaned_data['taskID']
            flag = form.cleaned_data['completedFlag']
            taskID = taskInfo.taskID
            taskInstance = task.objects.get(taskID = taskID)
            completedInstance = completed.objects.get(userID = userProfileInstance,taskID = taskInstance)
            completedFlag = completedInstance.completedFlag

            if not completedFlag and flag:
                addXP(request,user=currentUser,completedtask=taskID)
                return redirect('display')
            elif not completedFlag and not flag:
                pass
            elif completedFlag and flag:
                messages.success(request,'Task is Already Completed')
            elif completedFlag and not flag:
                pass
            

        #create instance of completed with userid and task id
        #if form is valid and completedflag = false and post is true update completed flag, call addXP function
        #if form is valid completed flag = false and post is false do nothing
        #if form is valid and completed flag = true and post is true do nothing, send message
        #if form is valid and completed flag=true and post is false, remove xp
        

        


    return render(request,'schedule.html',context)


def editSchedule(request):
    addTaskForm = addTask()
    context = {
        'addTaskForm' : addTaskForm,
    }
    currentUser = request.user
    scheduleInstance = schedule.objects.get(user = currentUser)
    if request.method == 'POST':

        form = addTask(request.POST,instance=scheduleInstance)
        
        if form.is_valid():
            tasks = form.save(commit=False)
            tasks.user = currentUser
            form.save()

            taskIDs = form.cleaned_data['taskID']
            
            for taskID in taskIDs:
                IDs = taskID.taskID
                
                userInstance = User.objects.get(username = currentUser)
                userProfileInstance = userProfile.objects.get(user = userInstance)
                taskInstance = task.objects.get(taskID=IDs)

                if not completed.objects.filter(userID = userProfileInstance,taskID=IDs).exists():
                    completed.objects.create(userID = userProfileInstance,taskID=taskInstance)

            return redirect('display')
        else:
            messages.success(request, form.errors)
            messages.success(request, 'Failed to Add Task')

    return render(request,'editSchedule.html',context)