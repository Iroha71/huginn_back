from rest_framework import routers
from api_app.views import ProjectViewSet, TaskViewSet, DomainViewSet
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'domains', DomainViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('get_work_progress/<int:project_id>', views.calc_work_progress, name = 'calc_progress'),
]