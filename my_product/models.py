from django.db import models
from product.models import SubCategory
# Create your models here.


class MyProduct(models.Model):
    product_name = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    price = models.IntegerField(default=0)
    sub_category= models.ManyToManyField(SubCategory)
    
    def __str__(self):
        return self.product_name
