from django.db import models


# Create your models here.
class Custom(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)

    class Meta:
        abstract = True


class ClassLevel(models.Model):
    level = models.CharField(max_length=8)

    def __str__(self):
        return self.level


class Student(Custom):
    class_level = models.ForeignKey(ClassLevel, on_delete=models.PROTECT, default='', related_name='study_on')
    roll = models.PositiveIntegerField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class Teacher(Custom):
    teach = models.ManyToManyField(ClassLevel)
    joined = models.DateField(auto_now=True)

    def teaching(self):
        return ", ".join([str(p) for p in self.teach.all()])
