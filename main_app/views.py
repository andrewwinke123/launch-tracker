from django.shortcuts import render
from .models import Launch
from django.views.generic.edit import CreateView
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