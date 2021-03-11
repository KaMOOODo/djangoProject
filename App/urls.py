from django.urls import path

from App.views import *

urlpatterns = [
    path('about', about, name='about'),
    path('', main_page, name='home'),
    path('sign_in', signin, name='sign_in'),
    path('log_in', log_in),
    path('log_out', log_out, name='log_out'),
    path('sign_up', signup),
    path('reg', sign_up),
    path('validate', validate),
    path('item/<int:pk>/add_comment', add_comment),
    path('item/<int:pk>/', item_detail),
    path('curent_currencies', curent_currencies, name='curs'),
    path('test', item_detail),
    path('item/<int:item_id>/checkout', checkout, name='checkout'),
    path('item/<int:item_id>/checkout_submit', checkout_submit, name='checkout_submit'),
]