from rest_framework import serializers
from api_app.models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('name',)
