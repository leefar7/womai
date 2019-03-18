import hashlib
import random
import time

from django.core.cache import cache
from django.shortcuts import render, redirect

# Create your views here.


from app.models import Wheel, Shop, User


def index(request):
    user=None
    token  = request.session.get('token') #先拿到客户端保存的token
    userid=cache.get(token)  #再拿（缓存中）中保存的token
    if userid :   #如果缓存中有token

        user=User.objects.get(pk=userid)   #拿到与token对应用户对象

    whells = Wheel.objects.all()
    shop = Shop.objects.all()
    data={
        'user':user,
        'whells':whells,
        'shop':shop

    }
    return render(request,'index/index.html',context=data)
    # token = request.session.get('token')
    # userid = cache.get(token)
    #
    # if userid:
    #     userid = cache.get(token)
    #     user = User.objects.get(pk=userid)
    #     whells = Wheel.objects.all()
    #     shop = Shop.objects.all()
    #     data = {
    #         'whells': whells,
    #         'shops': shop,
    #         'user': user,
    #     }
    #
    #     return render(request, 'index/index.html', context=data)
    # else:
    #
    #
    #     return render(request, 'index/index.html')







def getmd5_password(param):
    md5 = hashlib.md5()
    md5.update(param.encode('utf-8'))
    return md5.hexdigest()


def get_token():
    temp = str(time.time()) + str(random.random())
    md5 = hashlib.md5()
    md5.update(temp.encode('utf-8'))
    return md5.hexdigest()


def register(request):
    data = {

    }
    if request.method == 'GET':
        return render(request, 'mine/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        nickname = request.POST.get('nickname')

        user = User()
        user.username = username
        user.password = getmd5_password(password)
        user.phone = phone
        user.nickname = nickname
        user.save()

        token = get_token()
        cache.set(token, user.id, 60 * 60 * 24 * 7)
        request.session['token'] = token
        return redirect('womai:index')


def login(request):
    if request.method=='GET':
        return render(request,'mine/Login.html')

    elif request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = User.objects.filter(username=username)
        if users.exists():#存在
            user  = users.first()
            if user.password==getmd5_password(password):
                token=get_token()
                cache.set(token,user.id,60*60*24*3)
                request.session['token']=token
                return redirect('womai:index')
            else:
                return render(request,'mine/Login.html',context={'err':'密码错误'})
        else:
            return render(request, 'mine/Login.html', context={'err': '用户不存在'})




def logout(request):
    request.session.flush()
    return redirect('womai:index')
