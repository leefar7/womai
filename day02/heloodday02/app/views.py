import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Student


def index(request):
    return HttpResponse('美团app首页')



def addstu(request):
    stu = Student()
    stu.s_name=str(random.randrange(1,100000))+'张三'
    stu.s_score=random.randrange(1,100)
    stu.s_weight=75.00000222231
    stu.s_height=180.333333
    stu.s_detail='hello world'
    stu.s_math=random.randrange(1,100)
    stu.s_english=random.randrange(1,100)
    stu.save()

    return HttpResponse('添加学生成功:'+stu.s_name)

