from django.shortcuts import render, HttpResponse
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.models import  User
from django.http import HttpResponseRedirect, JsonResponse
import re
import requests
import json
from django.utils.translation import ugettext as trans, activate


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
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Неверный логин, пароль или эмейл')

    # user_login = authenticate(username = user[0], passwrod = user[1])

    # return HttpResponse('Ok!')


def validate_login(request):
    username = request.POST['login']
    if username is not None:
        data = {
            'message': User.objects.filter(username=username).exists()
        }
    return JsonResponse(data)



def validate_email(request):
    email = request.POST['email']
    if email is not None:
        data = {
            'email': User.objects.filter(email=email).exists()
        }
    return JsonResponse(data)


def curent_currencies(requset):
#зарендерить выпадающим меню
    course = requests.get('https://www.nbrb.by/api/exrates/rates/dynamics/145?startdate=2020-10-13&enddate=2020-10-20')
    data = json.loads(course.text)
    sum_course = 0
    for cur_day in data:
        sum_course += cur_day['Cur_OfficialRate']
    return HttpResponse('Курс доллара: ' + str(round((sum_course/7),2)))
    # context = {
    #         'currencies_name' : data['Cur_Name'],
    #         'course' : data['Cur_OfficialRate']
    #     }
    # return render(requests, 'index.html', context)

def change_language_eng(request):
    print(request.POST['lang'])
    activate('en')
    print('now eng language')
    return HttpResponseRedirect('/')
