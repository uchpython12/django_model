from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.http import HttpResponse

from django.shortcuts import render
from .models import YourModel

def index(request):
    return JsonResponse({'message': 'Welcome to the homepage!'})

def other_view(request):
    return HttpResponse("This is the other view!")

def home(request):
    return render(request, 'home.html')

# views.py



def read_data(request):
    data = YourModel.objects.all()
    # 创建一个新的 YourModel 实例
    # new_instance = YourModel(name='John', age=30, email='john@example.com')
    # new_instance.save()  # 保存实例到数据库中
    return render(request, 'read_data.html', {'data': data})
