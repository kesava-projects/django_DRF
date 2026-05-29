from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    def validate_name(self, value):
        data = Student.objects.filter(name=value)
        if data.exists():
            raise serializers.ValidationError("Student with this name already exists")
        return value

    def validate_phone(self, value):
        if len(value) != 10:
            raise serializers.ValidationError("phone number must be 10 digits")
        return value


