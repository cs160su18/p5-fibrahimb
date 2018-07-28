from django.contrib import admin
from life.models import *

class AdminSend(admin.ModelAdmin):
  list_display = ('name', 'email', 'phone', 'date')

class AdminJobs(admin.ModelAdmin):
  list_display = ('job_title', 'description')
# Register your models here.
admin.site.register(Group)
admin.site.register(Send, AdminSend)
admin.site.register(Jobs, AdminJobs)
