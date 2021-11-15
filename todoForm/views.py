from django.shortcuts import render
from .serializers import TodoSerializer, Todo_validationSerializer
from rest_framework import viewsets
from .models import Todo_model, Validation_model


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo_model.objects.all()


class Validation_serializerView(viewsets.ModelViewSet):
    serializer_class = Todo_validationSerializer
    queryset = Validation_model.objects.all()

# Create your views here.
