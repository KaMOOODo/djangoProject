from django.urls import path

from App.views import *

urlpatterns = [
    path('about', about, name='about'),
    path('', main_page, name='home'),
    path('sign_in', signin),
    path('log_in', log_in),
    path('log_out', log_out),
    path('sign_up', signup),
    path('reg', sign_up),
    path('validate', validate),
    path('item/<int:pk>/add_comment', add_comment),
    path('item/<int:pk>/', item_detail),
    path('curent_currencies', curent_currencies, name='curs'),
    path('test', item_detail)
]