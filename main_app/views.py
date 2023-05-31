from django.shortcuts import render

from django.http import HttpResponse


class Rocket:
  def __init__(self, mission, model, mfg, size, orbit, crew, payload, location, date):
    self.mission = mission
    self.model = model
    self.mfg = mfg
    self.size = size
    self.orbit = orbit
    self.crew = crew
    self.payload = payload
    self.location = location
    self.date = date

rockets = [
  Rocket('ROCKET LIKE A HURRICANE', 'Electron', 'Rocket Lab', 'small', 'LEO', 0, 'NASA Tropics', 'NZ', 'May 8, 2023'),
  Rocket('ROCKET LIKE A HURRICANE', 'Electron', 'Rocket Lab', 'small', 'LEO', 0, 'NASA Tropics', 'NZ', 'May 8, 2023'),
  Rocket('ROCKET LIKE A HURRICANE', 'Electron', 'Rocket Lab', 'small', 'LEO', 0, 'NASA Tropics', 'NZ', 'May 8, 2023'),
  Rocket('ROCKET LIKE A HURRICANE', 'Electron', 'Rocket Lab', 'small', 'LEO', 0, 'NASA Tropics', 'NZ', 'May 8, 2023'),
]

# Define the home view
def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')

def launch_index(request):
  return render(request, 'launches/index.html', { 'rockets': rockets })