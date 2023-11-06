from product.models import *
from rest_framework import serializers


class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

class AllProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
    