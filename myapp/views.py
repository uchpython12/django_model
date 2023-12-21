from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.http import HttpResponse
def index(request):
    return JsonResponse({'message': 'Welcome to the homepage!'})

def other_view(request):
    return HttpResponse("This is the other view!")

