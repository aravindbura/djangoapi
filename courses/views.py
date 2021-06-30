from django.shortcuts import render
from rest_framework import viewsets
from .models import Course
from .serializer import CourseSerializer

class Courseview(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


