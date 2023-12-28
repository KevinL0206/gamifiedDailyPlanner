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

    
    tasks = scheduleInstance.taskID.all()
    context = {'tasks': tasks}

    return render(request,'schedule.html',context)
