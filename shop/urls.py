from django.urls import path
from .views import MenuList

app_name = 'shop'

urlpatterns = [
    path('menu/', MenuList.as_view(), name='menu'),
]