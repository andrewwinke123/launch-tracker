from django.contrib import admin
from .models import Launch, Schedule, Satellite, Photo

admin.site.register(Launch)
admin.site.register(Schedule)
admin.site.register(Satellite)
admin.site.register(Photo)