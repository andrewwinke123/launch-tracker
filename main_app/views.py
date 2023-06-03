from django.shortcuts import render, redirect
from .models import Launch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Launch
from .forms import ScheduleForm

class LaunchCreate(CreateView):
  model =  Launch
  fields = '__all__'

class LaunchCreate(CreateView):
  model = Launch
  fields = '__all__'
  success_url = '/launches/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def launch_index(request):
  launches = Launch.objects.all()
  return render(request, 'launches/index.html', { 'launches': launches })

def launch_detail(request, launch_id):
  launch = Launch.objects.get(id=launch_id)
  schedule_form = ScheduleForm()
  return render(request, 'launches/detail.html', { 'launch': launch, 'schedule_form': schedule_form })

def add_schedule(request, launch_id):
  form = ScheduleForm(request.POST)
  if form.is_valid():
    new_schedule = form.save(commit=False)
    new_schedule.launch_id = launch_id
    new_schedule.save()
  return redirect('launch-detail', launch_id=launch_id)

def add_schedule(request, launch_id):
  form = ScheduleForm(request.POST)
  if form.is_valid():
    new_schedule = form.save(commit=False)
    new_schedule.launch_id = launch_id
    new_schedule.save()
  return redirect('launch-detail', launch_id=launch_id)

class LaunchUpdate(UpdateView):
  model = Launch
  fields = [
  'model',
  'mfg',
  'size',
  'orbit',
  'crew',
  'payload',
  'location',
  'date'
  ]

class LaunchDelete(DeleteView):
  model = Launch
  success_url = '/launches/'