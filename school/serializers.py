from rest_framework import serializers
from .models import Student, Teacher, ClassLevel


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        depth = 1


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        depth = 1


class ClassLevelSerializers(serializers.ModelSerializer):
    study_on = StudentSerializers(many=True, read_only=True)

    class Meta:
        model = ClassLevel
        fields = ['id', 'level', 'study_on']
