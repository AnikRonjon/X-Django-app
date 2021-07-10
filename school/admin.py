from django.contrib import admin
from .models import (ClassLevel, Student, Teacher)


# Register your models here.
@admin.register(ClassLevel)
class ClassLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'level')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll', 'email', 'class_level')


@admin.register(Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ('name', 'email', 'joined', 'teaching')
