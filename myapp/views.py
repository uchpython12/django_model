from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.http import HttpResponse

from .models import YourModel
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
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

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            return redirect('login')
    else:
        form = RegistrationForm()  # 创建一个空的表单

    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        # 处理表单提交
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # 登录成功后的重定向或其他操作
            return redirect('dashboard')  # 替换为你的登录成功后的 URL 名称
        else:
            pass
            # 处理登录失败的情况
            # ...
    else:
        # 处理 GET 请求的情况
        return render(request, 'login.html')