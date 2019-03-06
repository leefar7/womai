import math

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Goods


def index(request,num):
    goods_list =Goods.objects.all()
    # 总页数
    total_page = math.ceil(goods_list.count()/12)
    num = int(num)


    return render(request,'index.html')