from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from . import models
from .serializers import *


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

