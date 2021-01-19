from django.shortcuts import render

from rest_framework import viewsets, generics
from .serializers import TodoSerializer

from .models import TodoModel


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()


class TodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()


class TodoDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()
