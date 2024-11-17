from django.urls import path, include
from .views import hello_PI_3
from .views import post_detail, ss_form

urlpatterns = [
    path('', hello_PI_3),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('ss-form/', ss_form, name='ss_form'),
]
