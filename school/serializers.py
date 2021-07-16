from rest_framework import serializers
from .models import Student, Teacher, ClassLevel


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'email', 'class_level', 'roll')
        depth = 1


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('name', 'email', 'teach', 'joined')
        depth = 1


class ClassLevelSerializers(serializers.ModelSerializer):
    study_on = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='api_school:student-detail')

    class Meta:
        model = ClassLevel
        fields = ['id', 'level', 'study_on']
