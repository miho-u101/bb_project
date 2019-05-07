from django.db import models

# Create your models here.

class Cruiser(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=50)
    capacity = models.IntegerField(default=0)
    charge1 = models.IntegerField(default=0)
    charge2 = models.IntegerField(default=0)

#データ型
#CharField(max_length=100)
#IntegerField(default=0)
#DateField
#BooleanField
#EmailField(max_length=200)