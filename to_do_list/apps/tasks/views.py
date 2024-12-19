from django.shortcuts import render
from .models import Task
from rest_framework import viewsets, status
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()