from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Student, ClassLevel, Teacher
from .serializers import StudentSerializers, ClassLevelSerializers, TeacherSerializers


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'email']


class TeacherModelViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'email']


class ClassLevelModelViewSet(ModelViewSet):
    queryset = ClassLevel.objects.all()
    serializer_class = ClassLevelSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['level']

