from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .api_exceptions import StudentNotFoundException
from .models import Student
from .student_serializer import StudentSerializer

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_view(request):
    if request.method == 'POST':
        data = request.data
        student_serializer = StudentSerializer(data = data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data)
        else:
            return Response(student_serializer.errors)
    else:
        return Response({"message": "Method not allowed"})

@api_view(['PUT'])
def update_student(request, id):
    student_object = Student.objects.get(id=id)
    student_serializer = StudentSerializer(
        student_object,
        request.data
    )
    if student_serializer.is_valid():
        student_serializer.save()
        return Response({
            "message": "Data updated successfully",
        })
    return Response(student_serializer.errors)

@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student_object = Student.objects.get(id=id)
    except Exception as e:
        raise StudentNotFoundException()
    student_object.delete()
    return Response({
        "message": "Data deleted successfully"
    })

@api_view(['GET'])
def get_student(request, id):
    try:
        student_object = Student.objects.get(id=id)
    except Exception as e:
        raise StudentNotFoundException()

    return Response({
            "id": student_object.id,
            "name": student_object.name,
            "email": student_object.email,
            "phone": student_object.phone,
        })

@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

