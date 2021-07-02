from django.db import models

# Create your models here.

class Restaurant(models.Model):
    product = models.CharField(max_length=200)
    description=models.CharField(max_length=100)
    price=models.CharField(max_length=10)

    def __str__(self):
        return self.name

