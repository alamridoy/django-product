from django.db import models
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(blank=True,null=True,max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.category_name
    
class SubCategory(models.Model):
    brand_name = models.CharField(max_length=100,blank=True,null=True)
    sub_category_name = models.CharField(max_length=100,blank=True,null=True)
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sub_category_name
