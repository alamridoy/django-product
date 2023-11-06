from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from my_product.models import *
from my_product.serializers import MyProductSerilizer 
from rest_framework import status


# Create your views here.
@api_view(['POST'])
def product_add(request):
    if request.method == 'POST':
        data = request.data
      
        product_serializer = MyProductSerilizer(data=data)
      
        if product_serializer.is_valid():
           
            product_serializer.save()
            create_data = {
                "status":201,
                "success":True,
                "message":"Product successfully created!",
                "data": product_serializer.data
            }
         
            return Response(create_data,status.HTTP_201_CREATED)
        return Response(product_serializer.errors)


#list
@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        products = MyProduct.objects.all()
        list_serializer = MyProductSerilizer(products,many=True)
        list = {
            "status":200,
            "success":True,
            "message":"Product List",
            "data":list_serializer.data
        }
        return Response(list,status.HTTP_200_OK)
    


#details
@api_view(['GET'])
def product_details(request,id):
    if request.method == 'GET':
        products = MyProduct.objects.filter(id=id)
        details_serializer = MyProductSerilizer(products,many=True)
        if products.exists():
            
            product_details = {
                    "status": 200,
                    "success":True,
                    "message": "Category details",
                    "data": details_serializer.data[0]
                    
                }
            return Response(product_details,status.HTTP_200_OK)
        else:
            return Response("Data not found",status.HTTP_404_NOT_FOUND)
       
    
#update
@api_view(['PUT'])
def product_update(request, id):
    try:
        product = MyProduct.objects.get(id=id)     
    except MyProduct.DoesNotExist:
        return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        product_serializer = MyProductSerilizer(product, data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            update_data = {
                "status": 200,  
                "success": True,
                "message": "Product successfully updated!",
                "data": product_serializer.data  
            }
         
            return Response(update_data, status=status.HTTP_200_OK)
        return Response(product_serializer.errors)


@api_view(['DELETE'])
def delete_product(request, id):
    try:
        item = MyProduct.objects.get(id=id)
        item.delete()
        return Response("Product  successfully deleted!",status=status.HTTP_202_ACCEPTED)
    except MyProduct.DoesNotExist:
        return Response("This Product not found", status=status.HTTP_404_NOT_FOUND)


