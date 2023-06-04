from django.contrib import admin
from .models import Launch, Schedule, Satellite

admin.site.register(Launch)
admin.site.register(Schedule)
admin.site.register(Satellite)