import hashlib
import random
import time

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app.models import User


def index(request):
    username = request.session.get('username')

    return render(request,'index.html',context={'usernmae':username})


def errtest(request):
    # print(a)
    return HttpResponse('错误测试')


def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    elif request.method=='POST':
        user = User()
        user.username=request.POST.get('username')
        user.password=request.POST.get('password')
        user.tel=request.POST.get('tel')
        user.save()
        response = redirect('app:index')
        request.session['username']=user.username
        return response


def logout(request):
    response=redirect('app:index')
    del request.session['username']
    return response


#生成token
#token 唯一标识
def generate_token():
    token = str(time.time())+str(random.randrange())
    md5=hashlib.md5()
    md5.update(token.encode('utf-8'))
    return md5.hexddigest()
