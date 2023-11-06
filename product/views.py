from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Category,SubCategory
from product.serializers import ProductSerilizer,AllProductSerilizer
from rest_framework import status

# Category crud
#create
@api_view(['POST'])
def create_category(request):
    if request.method == 'POST':
        data = request.data
        serializer = ProductSerilizer(data=data)
        check_duplicate = Category.objects.filter(category_name=request.data['category_name'])
        
        if not data:
              return Response("Data should not be empty", status=status.HTTP_400_BAD_REQUEST)
        
        elif check_duplicate.exists():
            
            return Response("This is duplicate value",status=status.HTTP_409_CONFLICT)
                
        else:
                if serializer.is_valid():
                    serializer.save()
                    create_data = {
                        "status":201,
                        "success":True,
                        "Message":"Categoty successflly added"
                    }
                    return Response(create_data,status=status.HTTP_201_CREATED)
                return Response(serializer.errors)

#list
@api_view(['GET'])
def list_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = ProductSerilizer(categories, many=True)
        return_data = {
                    "status": 200,
                    "success":True,
                    "message": "Category List",
                    "data": serializer.data
                    
                }
        return Response(return_data,status.HTTP_200_OK)
    
#details/id    
@api_view(['GET'])
def details_categories(request,id):
    if request.method == 'GET':
        category = Category.objects.filter(id=id)
        serializer = ProductSerilizer(category, many=True)
        
        if category.exists():
            
            return_data = {
                    "status": 200,
                    "success":True,
                    "message": "Category details",
                    "data": serializer.data[0]
                    
                }
            return Response(return_data,status.HTTP_200_OK)
        else:
            return Response("Data not found",status.HTTP_404_NOT_FOUND)
            
       
   
   
    
@api_view(['PUT'])
def update_category(request, id):
    item = Category.objects.get(id=id)
    serializer = ProductSerilizer(item, data=request.data)
    
    check_duplicate = Category.objects.filter(category_name=request.data['category_name'])
        
    if not serializer:
              return Response("Data should not be empty", status=status.HTTP_400_BAD_REQUEST)
        
    elif check_duplicate.exists():
            
            return Response("This is duplicate value",status=status.HTTP_409_CONFLICT)
    if serializer.is_valid():
        serializer.save()
        update_data = {
                        "status":201,
                        "success":True,
                        "Message":"Categoty successflly updated"
                    }
        return Response(update_data,status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    


@api_view(['DELETE'])
def delete_items(request, id):
    try:
        item = Category.objects.get(id=id)
        item.delete()
        return Response("Categoty successfully deleted!",status=status.HTTP_202_ACCEPTED)
    except Category.DoesNotExist:
        return Response("This Category not found", status=status.HTTP_404_NOT_FOUND)



# Product crud
#create
@api_view(['POST'])
def create_product(request):
    if request.method == 'POST':
        data = request.data
        product_serializer = AllProductSerilizer(data=data)
        if product_serializer.is_valid():
            product_serializer.save()
            create_data = {
                "status":201,
                "success":True,
                "message":"Product successfully created!",
                "data": product_serializer.data
            }
            print(create_data)
            return Response(create_data,status.HTTP_201_CREATED)
        return Response(product_serializer.errors)
            
#list
@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        products = SubCategory.objects.all()
        product_serializer_list = AllProductSerilizer(products, many=True)
        product_list = {
                    "status":200,
                    "success":True,
                    "message":"Products List",
                    "data": product_serializer_list.data
                }
        return Response(product_list,status.HTTP_200_OK)
    
#details
@api_view(['GET'])
def product_details(request,id):
    if request.method == 'GET':
        products = SubCategory.objects.filter(id=id)
        product_serializer_list = AllProductSerilizer(products, many=True)
        if products.exists():
            product_details = {
                        "status":200,
                        "success":True,
                        "message":"Products List",
                        "data": product_serializer_list.data[0]
                    }
            return Response(product_details,status.HTTP_200_OK)
        else:
            return Response("Product not found",status.HTTP_404_NOT_FOUND)
        
#update

    
@api_view(['PUT'])
def update_product(request, id):
    try:
        item = SubCategory.objects.get(id=id)
    except SubCategory.DoesNotExist:
        return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = request.data
        product_serializer = AllProductSerilizer(item, data=data)

        if product_serializer.is_valid():
            product_serializer.save()
            update_data = {
                "status": 201,
                "success": True,
                "message": "Product successfully updated!",
                "data": product_serializer.data
            }
            return Response(update_data, status=status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   

@api_view(['DELETE'])
def delete_product(request, id):
    try:
        item = SubCategory.objects.get(id=id)
        item.delete()
        return Response("Product  successfully deleted!",status=status.HTTP_202_ACCEPTED)
    except SubCategory.DoesNotExist:
        return Response("This Product not found", status=status.HTTP_404_NOT_FOUND)
