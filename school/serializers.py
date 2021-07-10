from rest_framework import serializers
from .models import Student, Teacher, ClassLevel


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
