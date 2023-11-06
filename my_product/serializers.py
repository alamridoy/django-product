from my_product.models import *
from rest_framework import serializers

        
class MyProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = MyProduct
        fields = '__all__'
    