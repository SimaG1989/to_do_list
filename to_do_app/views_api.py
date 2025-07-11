from rest_framework import viewsets,status
from rest_framework.response import Response
from .Serializers import TaskSerializer
from .models import Task
from rest_framework.decorators import action
from django.shortcuts import render, redirect, get_object_or_404

from  django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login



class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['status']

  def get_queryset(self):
    queryset = self.queryset

    status_filter = self.request.query_params.get('status')
    if status_filter:
      queryset = queryset.filter(status=status_filter)

    return queryset
  @action(detail=True, methods=['post'])
  def mark_completed(self, request,pk=None):
    task = self.get_object()
    task.status = 'Completed'
    task.save()
    return Response({"status": "completed"})

