from django.urls import path

from App.views import *

urlpatterns = [
    path('about', index),
    path('item_list', Item_list),
    path('', main_page),
    path('sign_in', signin),
    path('log_in', log_in),
    path('log_out', log_out),
    path('sign_up', signup),
    path('reg', sign_up),
    path('validate_login', validate_login),
    path('validate_email', validate_email),
]