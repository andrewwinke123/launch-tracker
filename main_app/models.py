from django.db import models
from django.urls import reverse
import random
from django.contrib.auth.models import User


SCHEDULES = (
  ('M', 'Morning'),
  ('N', 'Noon'),
  ('D', 'Dusk')
)

def get_random_color():
    colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black', 'White', 'Purple', 'Orange', 'Grey', 'Pink']
    return random.choice(colors)

class Satellite(models.Model):
  name = models.CharField(max_length=50)
  company = models.CharField(max_length=50)
  description = models.CharField(max_length=50)
  duration = models.CharField(max_length=50)
  color = models.CharField(max_length=20, default = get_random_color)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('satellite-detail', kwargs={'pk': self.id})

class Launch(models.Model):
  mission = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  mfg = models.TextField(max_length=50)
  size = models.IntegerField()
  orbit = models.CharField(max_length=50)
  crew = models.IntegerField()
  payload = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  date = models.DateField()
  satellites = models.ManyToManyField(Satellite)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.mission
  
  def get_absolute_url(self):
    return reverse('launch-detail', kwargs={'launch_id': self.id})
  
  def launched_today(self):
    return self.schedule_set.filter(date=date.today()).count() >= len(SCHEDULES)

class Schedule(models.Model):
  date = models.DateField('Schedule date')
  schedule = models.CharField(
		max_length=1,
		choices=SCHEDULES,
		default=SCHEDULES[0][0]
  )
  launch = models.ForeignKey(Launch, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_schedule_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=250)
  launch = models.OneToOneField(Launch, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for launch_id: {self.launch_id} @{self.url}"