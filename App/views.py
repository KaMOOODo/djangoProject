from django.shortcuts import render, HttpResponse
from django.contrib.auth import  authenticate, login, logout
from django.http import HttpResponseRedirect

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

def log_in(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is None:
        return render('error.html', {})
    else:
        login(request, user)
        return HttpResponseRedirect('/')


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('is not sign in')


def signin(request):
    return render(request, 'sign_in.html')

def signup(request):
    return render(request, 'sign_up.html')

