from django.db import models
from django.urls import reverse

SCHEDULES = (
  ('M', 'Morning'),
  ('N', 'Noon'),
  ('D', 'Dusk')
)

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

  def __str__(self):
    return self.mission
  
  def get_absolute_url(self):
    return reverse('launch-detail', kwargs={'launch_id': self.id})

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