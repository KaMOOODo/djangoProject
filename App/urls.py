from django.urls import path, include

from App.views import *

urlpatterns = [
    path('about', index),
    path('item_list', Item_list),
]