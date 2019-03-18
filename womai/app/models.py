from django.db import models

# Create your models here
# 轮播图
class Wheel(models.Model):
    img = models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    class Meta:
        db_table='womai_wheel'

# //首页部分商品
class Shop(models.Model):

    img = models.CharField(max_length=100)
    typeid= models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    typename = models.CharField(max_length=100)
    class Meta:
        db_table='womai_shop'
'''
sql插入数据代码
insert into womai_shop(img,name,info,price,typeid,typename) values
("/static/img/indeximg/mad-01.jpg","维多丽白肉蜜柚2粒礼盒装","2.4-2.8kg | 肉清甜,水分含量适",'￥ 29.9','1001','我买特色'),
("/static/img/indeximg/mad-02.jpg","维多丽白肉蜜柚2粒礼盒装","2.4-2.8kg | 肉清甜,水分含量适",'￥ 29.9','1001','我买特色'),
("/static/img/indeximg/mad-03.jpg","维多丽白肉蜜柚2粒礼盒装","2.4-2.8kg | 肉清甜,水分含量适",'￥ 29.9','1001','我买特色'),
("/static/img/indeximg/mad-04.jpg","维多丽白肉蜜柚2粒礼盒装","2.4-2.8kg | 肉清甜,水分含量适",'￥ 29.9','1001','我买特色'),
("/static/img/indeximg/mad-05.jpg","维多丽白肉蜜柚2粒礼盒装","2.4-2.8kg | 肉清甜,水分含量适",'￥ 29.9','1001','我买特色'),
("/static/img/indeximg/mad-06.jpg","维多丽白肉蜜柚2粒礼盒装","2.4-2.8kg | 肉清甜,水分含量适",'￥ 29.9','1001','我买特色');

'''
# 用户 模型类
class User(models.Model):
    # 手机号
    phone = models.CharField(max_length=100,default='')
    # 用户名
    username=models.CharField(max_length=100,unique=True)
    # 邮箱
    email = models.CharField(max_length=100)
    # 密码
    password = models.CharField(max_length=256)
    # 昵称
    nickname = models.CharField(max_length=100)
    # 头像
    img = models.CharField(max_length=100, default='axf.png')
    # 等级
    rank = models.IntegerField(default=1)

    class Meta:
         db_table = 'womai_user'