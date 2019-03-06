import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#视图函数,第一个参数必须是request


from meituan.models import Student


def index(request):
    return HttpResponse('首页')


def home(request):
    return HttpResponse('<h1>home页面</h1><p>hello</p>')


def cart(request):
    return render(request,'cart.html')


def addstu(request):
    stu = Student()
    stu.name=str(random.randrange(1,1000000))+'李白'
    stu.score=random.randrange(1,100)
    stu.save()
    return HttpResponse('添加学生-'+stu.name)
