from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def user_def_serializer(req):
    if req.method=='GET':
        data=student.objects.all()
        d=user_serializer(data,many=True)
        return JsonResponse(d.data,safe=False)
@csrf_exempt
def fun1(req):
    if req.method=='GET':
        data=student.objects.all()
        d=model_serializer(data,many=True)
        return JsonResponse(d.data,safe=False)
    elif req.method=='POST':
        d=JSONParser().parse(req)
        data=model_serializer(data=d)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data)
        else:
            return JsonResponse(data.errors)