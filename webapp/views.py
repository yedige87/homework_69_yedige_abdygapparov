# Create your views here.
import json

from django.http import JsonResponse


def json_add_view(request, *args, **kwargs):
    if request.body:
        vals = json.loads(request.body)
        a = vals['A']
        b = vals['B']
        return JsonResponse({"answer": a+b})
    return JsonResponse('error: 400 BadRequest')


def json_subtract_view(request, *args, **kwargs):
    if request.body:
        vals = json.loads(request.body)
        a = vals['A']
        b = vals['B']
        return JsonResponse({"answer": a - b})
    return JsonResponse('error: 400 BadRequest')


def json_multiply_view(request, *args, **kwargs):
    if request.body:
        vals = json.loads(request.body)
        a = vals['A']
        b = vals['B']
        return JsonResponse({"answer": a * b})
    return JsonResponse('error: 400 BadRequest')


def json_divide_view(request, *args, **kwargs):
    if request.body:
        vals = json.loads(request.body)
        a = vals['A']
        b = vals['B']
        return JsonResponse({"answer": a / b})
    return JsonResponse('error: 400 BadRequest')

