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

