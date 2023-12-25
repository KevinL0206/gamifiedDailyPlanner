from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(userProfile)
admin.site.register(category)
admin.site.register(task)
admin.site.register(schedule)
admin.site.register(completed)