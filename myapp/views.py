from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.http import HttpResponse

from .models import YourModel
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required

def index(request):
    return JsonResponse({'message': 'Welcome to the homepage!'})

def other_view(request):
    return HttpResponse("This is the other view!")

def home(request):
    return render(request, 'home.html')

@login_required
def success(request):
    return render(request, 'success.html')
# views.py



def read_data(request):
    data = YourModel.objects.all()
    # 创建一个新的 YourModel 实例
    # new_instance = YourModel(name='John', age=30, email='john@example.com')
    # new_instance.save()  # 保存实例到数据库中
    return render(request, 'read_data.html', {'data': data})


from django.contrib.auth.models import User
from django.db import IntegrityError

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        group_id = request.POST['group']

        # 检查用户名是否已存在
        if User.objects.filter(username=username).exists():
            error_message = "该用户名已被使用，请选择其他用户名。"
            groups = Group.objects.all()
            return render(request, 'register.html', {'groups': groups, 'error_message': error_message})

        # 其他注册逻辑...
    else:
        groups = Group.objects.all()
        return render(request, 'register.html', {'groups': groups})



from django.contrib import messages

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
            # 添加錯誤提示
            messages.error(request, '登录失败，请检查用户名和密码是否正确')
            return render(request, 'login.html')
    else:
        # 處理 GET 請求的情況
        return render(request, 'login.html')
