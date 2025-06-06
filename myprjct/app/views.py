from django.shortcuts import render
from rest_framework import viewsets
from .models import*
from .serializers import CourseSerializers

# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

# class StudentsViewSet(viewsets.ModelViewSet):
#     queryset = Students.objects.all()
#     serializer_class = StudentsSerializers