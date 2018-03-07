from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Client
from django.core.exceptions import ObjectDoesNotExist
import json, string, random
# Create your views here.
def secret_generator(size=10,chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def index(request):
    return HttpResponse("Hello, world. Welcome to Muhammad Ghozi's oauth webservice.")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        return JsonResponse({'status':'WIP'},status=200)
    else :
        response = {
            'status': 'Error',
            'description': 'Bad Request'
        }
        return JsonResponse(response,status=400)
def register(request):
    if request.method == 'POST':
        try :
            username = request.POST['username']
            password = request.POST['password']
            displayName = request.POST['displayName']
        except Exception :
            response = {
                'status': 'Error',
                'description': 'Bad Request'
            }
            return JsonResponse(response,status=400)
        try :
            c = Client.objects.get(username=username)
            response = {
                'status': 'error',
                'description': 'User telah teregister'
            }
            return JsonResponse(response,status=409)
        except ObjectDoesNotExist :
            secret = secret_generator()
            c = Client(username=username,password=password,displayName=displayName,secret=secret)
            c.save()
            userId = c.id
            response={}
            response['status'] = 'ok'
            response['userId'] = userId
            response['displayName'] = displayName
            response['secret'] = secret
            return JsonResponse(response,status=200)
    else :
        response = {
            'status': 'Error',
            'description': 'Bad Request'
        }
        return JsonResponse(response,status=400)
