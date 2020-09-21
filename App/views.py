from django.shortcuts import render, HttpResponse

from App.models import Items


def index(request):
    return HttpResponse("Лучший онлайн магазин!")

def Item_list(request):
    result = Items.objects.all()
    response = ''
    for x in result:
         response = x.name+ ' ' +response
    return HttpResponse(response)

def main_page(request):
    context = {
        'header' : 'Меню',
        'menu' : [
            'Каталог',
            'О нас',
            'admin'
        ]
    }
    return render(request, 'index.html', context)