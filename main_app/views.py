from django.shortcuts import render
from .models import Rocket
from django.views.generic.edit import CreateView
from .models import Rocket

class CatCreate(CreateView):
  model =  Rocket
  fields = '__all__'


def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')

def launch_index(request):
  rockets = Rocket.objects.all()
  return render(request, 'launches/index.html', { 'rockets': rockets })

def launch_detail(request, rocket_id):
  rocket = Rocket.objects.get(id=rocket_id)
  return render(request, 'launches/detail.html', { 'rocket': rocket })