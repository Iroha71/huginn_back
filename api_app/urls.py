from rest_framework import routers
from api_app.views import ProjectViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)