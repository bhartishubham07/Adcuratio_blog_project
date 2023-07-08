from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Shoe(models.Model):
    brand_name = models.CharField(max_length=50)
    shoe_name = models.CharField(max_length=50)
    shoe_image = models.ImageField(height_field=None, width_field=None, max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    website = models.URLField()
    description = models.TextField(default='Shoe')
    
    def __str__(self):
        return self.shoe_name
    