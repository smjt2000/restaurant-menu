"""
url file for shop app
"""
from django.urls import path
from .views import MenuList

app_name = 'shop'

urlpatterns = [
    path('', MenuList.as_view(), name='menu'),
]
