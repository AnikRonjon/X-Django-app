from django.urls import path, include
from . import api_views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('student', api_views.StudentModelViewSet, basename='student')
router.register('teacher', api_views.TeacherModelViewSet, basename='teacher')
router.register('class/level', api_views.ClassLevelModelViewSet, basename='class_level')

app_name = 'api_school'
urlpatterns = [
    path('', include(router.urls)),
]
