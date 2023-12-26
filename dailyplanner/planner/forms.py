from .models import *
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class addTask(forms.ModelForm):
    class Meta:
        model = schedule
        fields = ["taskID",]
        widgets = {
            'taskID': forms.Select(attrs={'class':'form-control'}),
        }


