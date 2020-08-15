from django.http import HttpResponse
from rest_framework import viewsets
from api_app.models import Project, Task, Domain
from api_app.serializers import ProjectSerializer, DomainSerializer, TaskSerializer
import json

# Create your views here.
class DomainViewSet(viewsets.ModelViewSet):
  queryset = Domain.objects.all()
  serializer_class = DomainSerializer

class ProjectViewSet(viewsets.ModelViewSet):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer

def calc_work_progress(request, project_id):
  total_tasks = Task.objects.filter(project_id = project_id).count()
  finished_tasks = Task.objects.filter(project_id = project_id, finished_date__isnull = False).count()
  work_progress = 0
  if finished_tasks != 0:
    work_progress = (finished_tasks / total_tasks) * 100
  
  params = { work_progress: work_progress }
  converted_param = json.dumps(params, ensure_ascii = False, indent = 2)
  return HttpResponse(converted_param)

