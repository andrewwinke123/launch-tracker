from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('launches/', views.launch_index, name='launch-index'),
  path('launches/<int:rocket_id>/', views.launch_detail, name='launch-detail'),
]