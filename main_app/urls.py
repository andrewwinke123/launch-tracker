from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('launches/', views.launch_index, name='launch-index'),
  path('launches/<int:launch_id>/', views.launch_detail, name='launch-detail'),
  path('launches/create/', views.LaunchCreate.as_view(), name='launch-create'),
  path('launches/<int:pk>/update/', views.LaunchUpdate.as_view(), name='launch-update'),
  path('launches/<int:pk>/delete/', views.LaunchDelete.as_view(), name='launch-delete'),
  path('launches/<int:launch_id>/add-schedule/', views.add_schedule, name='add-schedule'),
  path('satellites/create/', views.SatelliteCreate.as_view(), name='satellite-create'),
  path('satellites/<int:pk>/', views.SatelliteDetail.as_view(), name='satellite-detail'),
  path('satellites/', views.SatelliteList.as_view(), name='satellite-index'),
  path('satellitess/<int:pk>/update/', views.SatelliteUpdate.as_view(), name='satellite-update'),
  path('satellitess/<int:pk>/delete/', views.SatelliteDelete.as_view(), name='satellite-delete'),
  path('launches/<int:launch_id>/assoc-satellite/<int:satellite_id>/', views.assoc_satellite, name='assoc-satellite'),
  path('accounts/signup/', views.signup, name='signup'),
  path('logout/', views.logout_view, name='logout'),
  path('launches/<int:launch_id>/add-photo/', views.add_photo, name='add-photo'),
]