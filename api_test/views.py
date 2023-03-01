from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

from .models import Things

# Create your views here.

@require_http_methods(['GET'])
# @require_http_methods(['POST'])
def add_things(request):
    # return HttpResponse('ban')
    response={}
    try:
        things=Things(name=request.GET.get('name'))
        things.save()
        response['msg']='success'
        response['error_num']=0
    except Exception as e:
        response['msg']=str(e)
        response['error_num']=1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_things(request):
    response={}
    try:
        things=Things.objects.filter()
        response['list']=json.loads(serializers.serialize('json',things))
        response['msg']='success'
        response['error_num']=0
    except Exception as e:
        response['msg']=str(e)
        response['error_num']=1
    return JsonResponse(response)

