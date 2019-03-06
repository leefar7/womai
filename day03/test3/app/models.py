from django.db import models

# Create your models here.
from django.db.models import Manager


class AnimalManager(Manager):
    #重写
    def all(self):
        return super().all().exclude(isd_del=True)

class Animal(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    #逻辑删除
    isd_del = models.BooleanField(default=False)
    #如果没有自定义,系统默认object
    #object = models.Manager()
    myObjects = AnimalManager()
#一对一
# 一个人对应一个身份证
class Person(models.Model):
    p_name=models.CharField(max_length=40)

class IDCard(models.Model):
    i_no = models.CharField(max_length=40)
    #性别1男2女
    i_sex=models.IntegerField()
    i_addr=models.CharField(max_length=100)
    #声明关系(这个卡属于哪个人)
    i_person=models.OneToOneField(Person,models.SET_NULL,null=True)



# 一对多  一个班级对应多个学生
#===========================================#
#主表
class Grade(models.Model):
    g_name=models.CharField(max_length=40)

# 从表声明关系
class Student(models.Model):
    s_name=models.CharField(max_length=40)
    s_age=models.IntegerField()
    # 声明关系(这学生 属于 哪个班)
    s_grade = models.ForeignKey(Grade,models.SET_NULL,null=True)

class User(models.Model):
    username  = models.CharField(max_length=100,unique=True)





class Goods(models.Model):
    g_name =models.CharField(max_length=40)
    g_price=models.IntegerField()
    #多对多关系
    g_collection = models.ManyToManyField(User)
