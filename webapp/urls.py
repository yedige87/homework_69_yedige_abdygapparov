from django.urls import path

from webapp.views import json_add_view

urlpatterns = [
    path('add', json_add_view, name='add_view'),
]
