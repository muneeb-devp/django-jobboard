from django.urls import path
from . import views
from typing import List
from django.urls import URLPattern

urlpatterns: List[URLPattern] = [
  path('jobs', views.getJobs, name='getJobs'),
  path('jobs/<int:job_id>/', views.getJobById, name='getJobById')
]
