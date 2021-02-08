from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
import re
from App.models import Items, Comments
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return HttpResponse("Лучший онлайн магазин!")


def main_page(request):
    items = Items.objects.order_by('-id')
    comments = Comments.objects.order_by('date')
    context = {
        'items': items,
        'comments': comments
    }
    return render(request, 'index.html', context)


def log_in(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is None:
        return HttpResponse('Неверный логин или пароль')
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
    if (re.match('^\w+$',username) != None) and \
        (re.match('^\w+$', password)  != None) and \
        (re.match('^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', email)  != None):
        user = User.objects.create_user(
            request.POST['login'],
            password=request.POST['password'],
            email=request.POST['email'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name']
        )
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/')
    else:
        return redirect('/')


def validate_login(request):
    username = request.GET['login']
    if username is not None:
        data = {
            'message': User.objects.filter(username=username).exists()
        }
    return JsonResponse(data)


def validate_email(request):
    email = request.GET['email']
    if email is not None:
        data = {
            'email': User.objects.filter(email=email).exists()
        }
    return JsonResponse(data)


def validate_comment(request):
    comment = request.POST['TextComment']
    if comment is not None:
        return not Comments.objects.filter(text=comment).exists()


def add_comment(request):
    if request.method == 'POST' and validate_comment(request):
        form = CommentForm({
            'text': request.POST['TextComment'],
            'item_id': request.POST['ItemID'],
            'user_id': request.user.id
        })
        if form.is_valid():
            form.save()
            return redirect('/')
    return redirect('/')
