from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'chat/index.html')

def room(request):
    table_name = request.GET.get('table_name')
    template = 'chat/room.html'

    if table_name is None:
        table_name = request.COOKIES.get('table_name')

    if table_name == 'admin':
        template = 'chat/admin.html'

    return render(request, template, {'table_name': table_name})

