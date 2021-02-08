from django.urls import path

from App.views import *

urlpatterns = [
    path('about', index),
    path('', main_page, name='home'),
    path('sign_in', signin),
    path('log_in', log_in),
    path('log_out', log_out),
    path('sign_up', signup),
    path('reg', sign_up),
    path('validate_login', validate_login),
    path('validate_email', validate_email),
    path('validate_comment', validate_comment),
    path('add_comment', add_comment),
    path('curent_currencies',curent_currencies),
]