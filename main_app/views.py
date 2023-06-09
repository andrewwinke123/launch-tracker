from django.shortcuts import render, redirect
from .models import Launch, Satellite
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ScheduleForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Launch, Satellite, Photo
from django.core.exceptions import ObjectDoesNotExist
import uuid
import boto3
import json
from django import forms

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'launchtrackerbucket'

def logout_view(request):
	logout(request)
	return redirect('/')

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def launch_index(request):
	launches = Launch.objects.all().order_by('-id')
	launches_data = [
		{
			'title': launch.mission,
			'start': launch.date.isoformat(),
			'extendedProps': {
				'mission': launch.mission,
				'model': launch.model,
				'mfg': launch.mfg,
				'size': launch.size,
				'orbit': launch.orbit,
				'crew': launch.crew,
				'payload': launch.payload,
				'location': launch.location,
				'photo_url': None,
				'detail_url': reverse('launch-detail', kwargs={'launch_id': launch.id})
			}
		} 
		for launch in launches
	]

	for data in launches_data:
		try:
			launch = Launch.objects.get(mission=data['title'], date=data['start'])
			data['extendedProps']['photo_url'] = launch.photo.url
		except ObjectDoesNotExist:
			pass 

	return render(request, 'launches/index.html', {'launches': launches, 'launches_data': json.dumps(launches_data)})

def launch_detail(request, launch_id):
	launch = Launch.objects.get(id=launch_id)
	satellites_launch_doesnt_have = Satellite.objects.exclude(id__in = launch.satellites.all().values_list('id'))
	schedule_form = ScheduleForm()
	is_creator = False
	if request.user == launch.user:
		is_creator = True
	return render(request, 'launches/detail.html', { 'launch': launch, 'schedule_form': schedule_form, 'satellites': satellites_launch_doesnt_have, 'is_creator': is_creator })

@login_required
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

class LaunchCreate(LoginRequiredMixin, CreateView):
	model = Launch
	fields = [
		'mission',
		'model',
		'mfg',
		'size',
		'orbit',
		'crew',
		'payload',
		'location',
		'date',
		'satellites',
	]

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		form.instance.satellites.clear()
		return super().form_valid(form)

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		if 'user' in form.fields:
			form.fields['user'].widget = forms.HiddenInput() 
		return form

def assoc_satellite(request, launch_id, satellite_id):
	launch = Launch.objects.get(id=launch_id)
	launch.satellites.add(satellite_id)
	return redirect('launch-detail', launch_id=launch_id)

class LaunchDelete(LoginRequiredMixin, DeleteView):
	model = Launch
	success_url = '/launches/'

class SatelliteCreate(LoginRequiredMixin, CreateView):
	model = Satellite
	fields = '__all__'

class SatelliteList(LoginRequiredMixin, ListView):
	model = Satellite

class SatelliteDetail(DetailView):
	model = Satellite

class SatelliteUpdate(LoginRequiredMixin, UpdateView):
	model = Satellite
	fields = ['name', 'company', 'description', 'duration' 'color']

class SatelliteDelete(LoginRequiredMixin, DeleteView):
	model = Satellite
	success_url = '/satellites/'

class Home(LoginView):
	template_name = 'home.html'

def signup(request):
	error_message = ''
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('launch-index')
		else:
			error_message = 'Invalid sign up - try again'
	form = UserCreationForm()
	context = {'form': form, 'error_message': error_message}
	return render(request, 'signup.html', context)

@login_required
def add_photo(request, launch_id):
	launch = Launch.objects.get(id=launch_id)
	if request.user != launch.user:
		return redirect('launch-detail', launch_id=launch_id)
		
	photo_file = request.FILES.get('photo-file', None)
	if photo_file:
		s3 = boto3.client('s3')
		key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
		try:
			s3.upload_fileobj(photo_file, BUCKET, key)
			url = f"{S3_BASE_URL}{BUCKET}/{key}"
			photo = Photo(url=url, launch_id=launch_id)
			launch_photo = Photo.objects.filter(launch_id=launch_id)
			if launch_photo.first():
				launch_photo.first().delete()
			photo.save()
		except Exception as err:
			print('An error occurred uploading file to S3: %s' % err)
	
	return redirect('launch-detail', launch_id=launch_id)
