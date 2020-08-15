from django.db import models

# Create your models here.
class Domain(models.Model):
  name = models.CharField(max_length = 50)
  is_hidden = models.BooleanField(default = True)

  def __str__(self):
        return str(self.name)

  class Meta:
    db_table = 'domains'

class Project(models.Model):
  name = models.CharField(max_length = 50)
  desc = models.CharField(max_length = 200, null = True)
  password = models.CharField(max_length = 20, null = True)
  level = models.IntegerField(default = 1)
  domain = models.ForeignKey(Domain, on_delete = models.CASCADE)

  def __str__(self):
        return str(self.name)

  class Meta:
    db_table = 'projects'

class Task(models.Model):
  title = models.CharField(max_length = 100)
  desc = models.CharField(max_length = 500, null = True)
  finished_date = models.DateTimeField(null = True)
  project = models.ForeignKey(Project, on_delete = models.CASCADE)

  def __str__(self):
        return str(self.name)
  
  class Meta:
    db_table = 'tasks'