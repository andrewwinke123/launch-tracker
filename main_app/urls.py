from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('launches/', views.launch_index, name='launch-index'),
  path('launches/<int:launch_id>/', views.launch_detail, name='launch-detail'),
  path('launches/create/', views.LaunchCreate.as_view(), name='launch-create'),
]