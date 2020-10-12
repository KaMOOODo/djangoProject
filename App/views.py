from django.shortcuts import render, HttpResponse
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.models import  User
from django.http import HttpResponseRedirect, JsonResponse
import re

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
        return HttpResponse('Неверный логин или пароль')
        # return render('error.html', {})
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


def sign_up(request):
    username = request.POST['login']
    password = request.POST['password']
    email = request.POST['email']
    if (re.match('^\w+$',username) != None) and (re.match('^\w+$', password)  != None) and (re.match('^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', email)  != None):
        user = User.objects.create_user(
            request.POST['login'],
            password=request.POST['password'],
            email=request.POST['email'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name']
        )
    else: return HttpResponse('Неверный логин, пароль или эмейл')
    user.save()
    return HttpResponse('Ok!')


def validate_login(request):
    username = request.POST['login']
    print(username)
    if username is not None:
        data = {
            'message': User.objects.filter(username=username).exists()
        }
    print(data)
    return JsonResponse(data)



def validate_email(request):
    email = request.POST['email']
    print(email)
    if email is not None:
        data = {
            'email': User.objects.filter(email=email).exists()
        }
    print(data)
    return JsonResponse(data)

