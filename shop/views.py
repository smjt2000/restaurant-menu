from django.views.generic import ListView

from .models import MenuItem

# Create your views here.

class MenuList(ListView):
    queryset = MenuItem.objects.active()
