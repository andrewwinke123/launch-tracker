from django.db import models
from django.urls import reverse

class Launch(models.Model):
  mission = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  mfg = models.TextField(max_length=50)
  size = models.IntegerField()
  orbit = models.CharField(max_length=50)
  crew = models.IntegerField()
  payload = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  date = models.CharField()

  def __str__(self):
    return self.mission
  
  def get_absolute_url(self):
    return reverse('launch-detail', kwargs={'launch_id': self.id})