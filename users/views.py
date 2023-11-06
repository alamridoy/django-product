from django.shortcuts import render
from rest_framework.views import APIView
from users.serializers import *
from rest_framework.response import Response
from rest_framework import status
from users.models import *
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime

# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        creatred_data = {
            "status":201,
            "success":True,
            "Message":"Complete Succesfully registration",
            "data":serializer.data
        }
        return Response(creatred_data,status.HTTP_201_CREATED)
    
class LoginView(APIView):   
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        
        user = User.objects.filter(email=email).first()
        
        if user is  None:
            raise AuthenticationFailed("User not found!!")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Invalid password")
        
        payload = {
            'id': user.id,
            'name':user.first_name,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload,'secret',algorithm='HS256')
       
        
        response = {
            "message":"Login successfull",
            'token':token
        }
        return Response(response)
            
            
# class UserView(APIView):
#     def get(self,request):
#         token = request.COOKIES.get('token')
            
#         if not token:
#             raise AuthenticationFailed("Unauthenticated!")
#         try:
#             payload = jwt.decode(token,'secret',algorithm=['HS256'])
#         except jwt.ExpiredSignatureError:
                
#             raise AuthenticationFailed("Unauthenticated!")
            
#         user = User.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)
            
#         return Response(serializer.data)
    
    
            
