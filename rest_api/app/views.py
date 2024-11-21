from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import JsonResponse
# Create your views here.
def user_def_serializer(req):
    if req.method=='GET':
        data=student.objects.all()
        d=user_serializer(data,many=True)
        return JsonResponse(d.data,safe=False)