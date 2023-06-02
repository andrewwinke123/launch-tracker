from django.shortcuts import render
from .models import Launch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Launch

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
  return render(request, 'launches/detail.html', { 'launch': launch })

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