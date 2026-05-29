import jwt
from django.http import JsonResponse
from django.shortcuts import render
from jwt import InvalidTokenError, ExpiredSignatureError
from rest_framework import status
from rest_framework.response import Response
from .models import UserModel
SECRET_KEY = 'django-insecure-iwky+iutr@j%z%huxc%6tejz*sf#+ptm_!5i=t1$v@h&+zn8%0'


from .userserializer import UserSerializer
from rest_framework.decorators import api_view

# Create your views here.

def is_authenticated(func):
    def wrapper(request):
        auth_header=request.headers.get("Authorization")
        if auth_header is None:
            return Response({
                "message":"Token is missing"
            })
        else:
            token=auth_header.split(" ")[1]
            try:
                decoded_token = jwt.decode(
                    token,
                    SECRET_KEY,
                    algorithms=['HS256']
                )
                user = UserModel.objects.filter(email=decoded_token['email']).first()
                if user is None:
                    return Response({
                        "message": "User no longer exists"
                    })
                request.user = user

            except jwt.ExpiredSignatureError:
                return Response({
                    "message": "Token has expired"
                }, status=401)

            except jwt.InvalidTokenError:
                return Response({
                    "message": "Invalid token"
                }, status=401)

            return func(request)

    return wrapper


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
        return Response({
            "message": str(e)
        })

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

@api_view(['GET'])
@is_authenticated
def profile(request):
    return Response({
        "id": request.user.id,
        "email": request.user.email,
        "phone": request.user.phone
    })

@api_view(['PUT'])
@is_authenticated
def update_profile(request):
    request.user.phone = request.data['phone']
    request.user.save()
    return Response({'message': 'Profile Updated'})

@api_view(['DELETE'])
@is_authenticated
def delete_profile(request):
    user = UserModel.objects.get(id=request.user.id)
    user.delete()
    return Response({'message': 'User Deleted'})









