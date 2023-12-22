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
            # 使用 Django 內建的 User model 創建新用戶
            User.objects.create_user(username=username, password=password)
            return redirect('login')  # 註冊成功後重定向到登入頁面
    else:
        form = RegistrationForm()  # 創建一個空的表單

    return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        # 處理表單提交
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # 登錄成功後的重定向或其他操作
            return redirect('/')  # 替換為你的登入成功後的 URL 名稱
        else:
            # 處理登入失敗的情況
            # 可以在此處添加錯誤提示或其他處理
            pass
    else:
        # 處理 GET 請求的情況
        return render(request, 'login.html')