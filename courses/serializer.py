#this is our serializer page
#another comment
from django.db.models import fields
from rest_framework import serializers
from . models import Restaurant

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields =('id','url','product','description','price')
    