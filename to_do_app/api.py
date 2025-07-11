from rest_framework.routers import DefaultRouter
from .views_api import TaskViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

url_patterns=router.urls
