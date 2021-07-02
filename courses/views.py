from django.shortcuts import render
from rest_framework import viewsets
from .models import Restaurant
from .serializer import RestaurantSerializer
  
class Restaurantview(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer




