import jwt
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import UserModel
SECRET_KEY = 'django-insecure-iwky+iutr@j%z%huxc%6tejz*sf#+ptm_!5i=t1$v@h&+zn8%0'


from .userserializer import UserSerializer
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['POST'])
def register(request):
    try:
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            return Response(user_serializer.data)
        else:
            return Response(user_serializer.errors)

    except Exception as e:
        return Response(user_serializer.errors)

@api_view(['POST'])
def login(request):
    user_object = UserModel.objects.filter(email=request.data['email'])
    if not user_object.exists():
        return Response({'message': 'Invalid email'})
    if user_object.first().password == request.data['password']:
        payload = {
            "email": user_object.first().email,
            "phone": user_object.first().phone,
        }
        token = jwt.encode(
            payload, SECRET_KEY, algorithm='HS256'
        )
        return Response({'message': 'User logged in',
                         'token': token})
    return Response({'message': 'Invalid password'})






