from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime
from .functions import addXP, dateDiff
# Create your views here.



