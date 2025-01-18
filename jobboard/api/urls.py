from django.urls import path
from . import views

urlpatterns = [
  path('jobs', views.getJobs, name='getJobs'),
  path('jobs/<int:job_id>/', views.getJobById, name='getJobById')
]
