from django.urls import path
from . import views
from typing import List
from django.urls import URLPattern


urlpatterns: List[URLPattern] = [
  path('', views.home, name='home'),
  path('jobs/<int:job_id>/', views.job_detail, name='job_detail')
]
