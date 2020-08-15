from rest_framework import serializers
from api_app.models import Project, Task, Domain

class DomainSerializer(serializers.ModelSerializer):
  class Meta:
    model = Domain
    fields = ('name', 'is_hidden')

class ProjectSerializer(serializers.ModelSerializer):
  domain = DomainSerializer()
  class Meta:
    model = Project
    fields = ('name', 'desc', 'level', 'domain')

class TaskSerializer(serializers.ModelSerializer):
  project = ProjectSerializer()
  class Meta:
    model = Task
    fields = ('title', 'desc', 'finished_date', 'project')