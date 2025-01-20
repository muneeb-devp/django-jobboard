from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from json import loads
from os.path import join
from typing import List, Dict, Optional, Any
from django.http import HttpRequest


class JobService:
  @staticmethod
  def get_jobs() -> List[Dict[str, Any]]:
    with open(
      join(settings.BASE_DIR, 'api', 'data', 'jobs.json'),
      encoding='utf-8'
    ) as file:
      return loads(file.read())

  @staticmethod
  def get_job_by_id(job_id: int) -> Optional[Dict[str, Any]]:
    jobs = JobService.get_jobs()
    return next((job for job in jobs if job['id'] == job_id), None)


@api_view(['GET'])
def getJobs(request: HttpRequest) -> Response:
  jobs = JobService.get_jobs()
  return Response(jobs)


@api_view(['GET'])
def getJobById(request: HttpRequest, job_id: int) -> Response:
  job = JobService.get_job_by_id(job_id)
  if job is not None:
    return Response(job)
  else:
    return Response({'error': 'Job not found'}, status=404)
