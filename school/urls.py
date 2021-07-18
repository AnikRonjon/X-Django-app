from django.urls import path
from . import views

app_name = 'school'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('student/registration/', views.student_reg_view, name='student_registration'),
    path('accounts/profile/', views.profile, name='profile'),
]
