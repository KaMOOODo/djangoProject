import json
import re
import requests

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from App.models import Items, Comments
from .forms import CommentForm
from datetime import date


def about(request):
    born = date(1995, 12, 5)
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    context = {
        'age': age,
        'image': 'https://instagram.fgme1-1.fna.fbcdn.net/v/t51.2885-15/e35/87531999_244134023289514_3451152764461641296_n.jpg?'
                 '_nc_ht=instagram.fgme1-1.fna.fbcdn.net&_nc_cat=110&_nc_ohc=g8vUomKNIuQAX9RqjOG&tp=1&'
                 'oh=428bcf0cdb228d234718b1b9142b03f0&oe=604BF0E5',
    }
    return render(request, 'about.html', context)


def main_page(request):
    paginator = Paginator(Items.objects.order_by('-id'), 4)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        item_list = paginator.page(page)
    except(EmptyPage, InvalidPage):
        item_list = paginator.page(1)

    # Get the index of the current page
    index = item_list.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    # Get our new page range. In the latest versions of Django page_range returns
    # an iterator. Thus pass it to list, to make our slice possible again.
    page_range = list(paginator.page_range)[start_index:end_index]
    context = {
        'item_list': item_list,
        'page_range': page_range,
    }
    return render(request, 'index.html', context)


def log_in(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is None:
        return render(request, 'sign_in.html', {'message': 'Неверный логин или пароль'})
    else:
        login(request, user)
        return redirect('home')


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')


def signin(request):
    return render(request, 'sign_in.html')


def signup(request):
    return render(request, 'sign_up.html')


def sign_up(request):
    username = request.POST['login']
    password = request.POST['password']
    email = request.POST['email']
    valid_username = re.match('^\w+$', username) is not None
    valid_password = re.match('^\w+$', password) is not None
    validate_email = re.match('^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', email) is not None
    if valid_username and valid_password and validate_email:
        try:
            user = User.objects.create_user(
                request.POST['login'],
                password=request.POST['password'],
                email=request.POST['email'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name']
            )
        except Exception as IntegrityError:
            return render(request, 'sign_up.html',
                          {'message': 'Пользователь с таким именем аккаунта или email уже существует'})
        if user is not None:
            user.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        return render(request, 'sign_up.html',
                      {'message': 'Пожалуйста, используйте следующий набор символов a-z, A-Z, 0-9, _'})


def validate(request):
    username = request.GET.get('login')
    if username is not None:
        data = {
            'message': User.objects.filter(username=username).exists()
        }
    else:
        email = request.GET['email']
        data = {
            'email': User.objects.filter(email=email).exists()
        }
    return JsonResponse(data)


def validate_comment(request):
    comment = request.POST['TextComment']
    if comment is not None:
        return not Comments.objects.filter(text=comment).exists()


def add_comment(request, pk):
    if request.method == 'POST' and validate_comment(request):
        form = CommentForm({
            'text': request.POST['TextComment'],
            'item_id': request.POST['ItemID'],
            'user_id': request.user.id
        })
        if form.is_valid():
            form.save()
            return item_detail(request, pk)
    return item_detail(request, pk)


def item_detail(request, pk):
    item = Items.objects.get(pk=pk)
    comments = Comments.objects.filter(item_id=pk)
    context = {
        'item': item,
        'comments': comments
    }
    return render(request, 'comments.html', context)


def curent_currencies(requset):
    course = requests.get('https://www.nbrb.by/api/exrates/rates/dynamics/145?startdate=2021-02-07&enddate=2021-02-13')
    data = json.loads(course.text)
    sum_course = 0
    for cur_day in data:
        sum_course += cur_day['Cur_OfficialRate']
    return HttpResponse('Курс доллара: ' + str(round((sum_course / 7), 2)))
