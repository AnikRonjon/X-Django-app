from django.urls import path
from .consumer import *

ws_urlpatterns = [
    path('ws/some_url/', WSConsumer.as_asgi())
]