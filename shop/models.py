from django.db import models

# Create your models here.
class Products(models.Model):
    product_title = models.CharField(max_length=200)
    product_price = models.FloatField()
    discount_price = models.FloatField()
    product_category = models.CharField(max_length=200)
    product_desc = models.TextField()
    image = models.CharField(max_length=300)
    
    
    
    