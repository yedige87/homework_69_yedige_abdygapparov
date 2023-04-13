from django.urls import path

from webapp.views import json_add_view, json_subtract_view, json_multiply_view, json_divide_view, get_token_view, \
    index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('get_token', get_token_view),
    path('add', json_add_view, name='add_view'),
    path('subtract', json_subtract_view, name='subtract_view'),
    path('multiply', json_multiply_view, name='multiply_view'),
    path('divide', json_divide_view, name='divide_view'),
]
