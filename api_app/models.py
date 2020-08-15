from django.db import models

# Create your models here.
class Project(models.Model):
  name = models.CharField(max_length = 50)
  desc = models.CharField(max_length = 200, null = True)
  password = models.CharField(max_length = 20, null = True)
  level = models.IntegerField(default = 1)

class Task(models.Model):
  title = models.CharField(max_length = 100)
  desc = models.CharField(max_length = 500)
  finished_date = models.DateTimeField()
  project = models.ForeignKey(Project, on_delete = models.CASCADE)