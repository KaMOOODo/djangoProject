from django.urls import path, include

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
    path('v_l', validate_login)
]