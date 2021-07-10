from django.contrib import admin
from django.urls import path, include

admin.site.site_title = "Yam's site"
admin.site.site_header = "AptYam's Dashboard"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('school.urls', namespace='school')),
]
