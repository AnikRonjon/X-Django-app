from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_title = "Yam's site"
admin.site.site_header = "AptYam's Dashboard"

urlpatterns = [
    path('secret/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('auth/', include('rest_framework.urls')),
    path('captcha/', include('captcha.urls')),
    path('', include('school.urls', namespace='school')),
    path('api/', include('school.api_urls', namespace='api_school')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
