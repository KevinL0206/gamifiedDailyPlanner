from .models import *
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class addTask(forms.ModelForm):
    class Meta:
        model = schedule
        fields = ["taskID"]
        widgets = {
            'taskID': forms.CheckboxSelectMultiple,
        }

class TrueFalseDropdown(forms.Select):
    def __init__(self, attrs=None):
        choices = (
            (True, 'True'),
            (False, 'False'),
        )
        super().__init__(attrs, choices)

class completeTask(forms.ModelForm):
    class Meta:
        model = completed
        fields=['taskID','completedFlag']
        widgets = {
            'taskID': forms.Select(attrs={'class':'form-control'}),
            'completedFlag': TrueFalseDropdown()
        }

        