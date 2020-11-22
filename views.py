from django.shortcuts import render, redirect, HttpResponse
from app01 import models


# Create your views here.
# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('loginUsername')
        password = request.POST.get('loginPassword')
        user = models.UserInfo.objects.filter(user=username).values()
        if password == user[0]['pwd']:
            return redirect('/index/')
        else:
            return redirect('/login/')


# 注册
def register(request):
    if request.method == 'POST':
        username = request.POST.get('registerUsername')
        email = request.POST.get('registerEmail')
        password = request.POST.get('registerPassword')
        print(username, email, password)
        return redirect('/login/')
    else:
        return render(request, 'register.html')


# 主页
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        return HttpResponse('查了个寂寞')
