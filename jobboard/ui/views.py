from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import requests
from django.http import JsonResponse


def home(request: HttpRequest) -> HttpResponse:
  response = requests.get('http://localhost:8000/api/jobs')
  data = response.json()
  print(data)
  return render(request, 'home.html', {'jobs': data})

def job_detail(request: HttpRequest, job_id: int) -> JsonResponse:
  response = requests.get(f'http://localhost:8000/api/jobs/{job_id}')
  data = response.json()
  return render(request, 'job_detail.html', {'job': data})
