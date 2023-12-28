from . import views
from django.urls import path

urlpatterns = [

    path('schedule/',views.displaySchedule, name = 'display')

]