from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from home.serializers import PeopleSerilizer

@api_view(['GET','POST','PUT'])
def index(request):
    courses = {
        'Language': 'Python',
        'Frame Work':['django','flask','fastapi'],
        'learning':['doc','youtube']
    }
    
    if request.method == 'GET':
        print("You hit an GET method")
        print(request.GET.get('search'))
        return Response(courses)
    elif request.method == 'POST':
        data = request.data
        print("*****")
        print('data:',data)
        print("You hit an POST method")
        return Response(data)
    elif request.method == 'PUT':
        print("You hit an PUT method")
        return Response(courses)
    else:
        return Response('Unknown method')
    
    

@api_view(['GET', 'POST','PUT','PATCH','DELETE'])
def person(request):
    if request.method == 'GET':
        obj = Person.objects.all()
        serializer = PeopleSerilizer(obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerilizer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            print('datasssss',serializer.data)
            return Response(serializer.data)  
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerilizer(obj,data=data)
        
        if serializer.is_valid():
            serializer.save()
            print('datasssss',serializer.data)
            return Response(serializer.data)  
        return Response(serializer.errors) 
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerilizer(obj,data=data, partial = True)
        
        if serializer.is_valid():
            serializer.save()
            print('datasssss',serializer.data)
            return Response(serializer.data)  
        return Response(serializer.errors) 
    
    else:
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({"Message":"Data deleted successfully!"})  
         