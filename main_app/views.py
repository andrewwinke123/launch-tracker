from django.shortcuts import render

from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello 🚀</h1>')