from django.shortcuts import render
from django.core import serializers
from django import forms
from .forms import *
from django.contrib.auth import authenticate, login
from life.models import *

def index(request):
  return render(request, 'life/index.html')

def send(request):
    if request.method == 'POST':
        form = SendForm(request.POST)
        if form.is_valid():
            send = Send.create(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['phone'], form.cleaned_data['date'], form.cleaned_data['time'])
            send.save()
    else:
        form = SendForm()
    return render(request, 'life/send.html', {'form': form})
  

def jobs(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            jobs = Jobs.create(form.cleaned_data['job_title'], form.cleaned_data['description'])
            jobs.save()
    else:
        form = JobForm()
    return render(request, 'life/jobs.html', {'form': form})
  
def applications(request):
    return render(request, 'life/applications.html')
  
  
def listings(request):
  if request.method == "GET":
    all_groups = Jobs.objects.all()
  return render(request, 'life/listings.html', {'job_listing': all_groups}) 

def schedule(request):
  if request.method == "GET":
    all_groups = Send.objects.all()
  return render(request, 'life/schedule.html', {'schedule_listing': all_groups}) 

