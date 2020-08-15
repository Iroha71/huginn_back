from rest_framework import viewsets, routers
from api_app.models import Project, Task
from api_app.serializers import ProjectSerializer

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()