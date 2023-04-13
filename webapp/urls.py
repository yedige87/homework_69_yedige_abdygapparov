from django.urls import path

from webapp.views import json_add_view, json_subtract_view

urlpatterns = [
    path('add', json_add_view, name='add_view'),
    path('subtract', json_subtract_view, name='subtract_view'),
]
