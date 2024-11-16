from django.urls import path, include
from .views import hello_PI_3

urlpatterns = [
    path('', hello_PI_3)
]
