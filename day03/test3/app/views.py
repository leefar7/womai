import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Animal, Person, IDCard, Grade, Student, User, Goods


def index(request):
    return render(request, 'index.html')


def animal(request):
    return render(request,'animal.html')





def addanimal(request):
    animal=Animal()
    animal.name='猫猫狗狗'+str(random.randrange(1,100000))
    animal.age=random.randrange(1,10)
    animal.save()

    return HttpResponse('添加动物成功')


def selectanimal(request):
    animals = Animal.myObjects.all()
    animal_str=''
    for  i in animals:
        animal_str +='<p> {}-{}-{} </p>'.format(i.id,i.name,i.age)
    print(len(animals))
    return HttpResponse(animal_str)


def deleteanimal(request):
    animal = Animal.myObjects.last()
    animal.delete()
    return HttpResponse('删除数据成功')
def updateanimal(request):
    animal = Animal.myObjects.last()
    animal.name='小花猫'
    animal.save()
    return HttpResponse('修改数据成功')


def onetoone(request):
    return render(request,'onetooen.html')


def addperson(request):
    person = Person()
    person.p_name='小白-'+str(random.randrange(1,100))
    person.save()


    return HttpResponse('添加成功:'+person.p_name)


def bindcard(request):
    card =IDCard()
    card.i_no='434343{}{}{}{}'.format(random.randrange(1900,2020),
                                      random.randrange(1, 13),
                                      random.randrange(1, 31),
                                      random.randrange(1000, 10000))
    card.i_sex=random.randrange(1,3)
    card.i_addr='深圳市南山区西丽镇{}号'.format(random.randrange(1,1000000))
    person=Person.objects.last()
    card.i_person=person
    card.save()
    return HttpResponse("身份证绑定成功")


def deleteperson(request):


    person =Person.objects.last()
    person.delete()


    return HttpResponse('删除人成功')

#获取卡对应的人信息(主表获取从表)
def selectcard(request):
    person = Person.objects.last()
    card = person.idcard
    if card.i_sex ==1:
        tem='男'
    else:
        tem='女'

    response_str='姓名{},性别{},身份证{},家庭住址{}'.format(person.p_name,tem,card.i_no,card.i_addr)
    return HttpResponse(response_str)

#获取人对应的卡信息(从表获取主表)
def selectperson(request):

    card = IDCard.objects.last()
    person = card.i_person
    if card.i_sex ==1:
        tem='男'
    else:
        tem='女'

    response_str='姓名{},性别{},身份证{},家庭住址{}'.format(person.p_name,tem,card.i_no,card.i_addr)
    return HttpResponse(response_str)

# 删卡
def deletecard(request):
    card = IDCard.objects.last()
    card.delete()
    return HttpResponse('删除成功')


def onetoduo(request):
    return render(request,'onetoduo.html')


def addgrade(request):
    grade =Grade()
    grade.g_name='python{}'.format(random.randrange(1801,1900))
    grade.save()



    return HttpResponse('班级添加成功:'+grade.g_name)


def addstu(request):
    stu = Student()
    names=['张三','李四','王五','马六','赵七','孙八']
    temp = random.randrange(0,len(names))
    stu.s_name=names[temp]+'-'+str(random.randrange(10,100))


    stu.s_age=random.randrange(18,38)
    # 班级

    grade=Grade.objects.last()

    stu.s_grade=grade

    stu.save()
    return HttpResponse('添加学生成功')


def deletegrade(request):
    grade=Grade.objects.last()
    grade.delete()

    return HttpResponse('删除班级成功')


def deletestu(request):
    stu=Student.objects.last()
    stu.delete()
    return HttpResponse('删除学生成功')

# 查询最后一个班级的信息 (主表查从表) 模型类中没有对应的属性 模型类小写
def selectgrade(request):
    grade = Grade.objects.last()
    stu=grade.student_set.all()
    stu_str='<h3>{}班级-学生人数:{}</h3>'.format(grade.g_name,stu.count())
    for st in stu:
        stu_str+='<p>{}-学生姓名-{}学生年龄-{}</p>'.format(st.id,st.s_name,st.s_age)
    return HttpResponse(stu_str)






def register(request):
    if request.method=='get':


        return render(request,'register.html')
    elif request.method=='post':
        username = request.POST.get('username')
        print(username)
        return HttpResponse('正在注册...')

# 查询学生信息(对应的班级) (从表查主表)
def selectstu(request):
    stu=Student.objects.all()

    str=''

    for st in stu:
        grade = st.s_grade
        if grade:

            str+='<p>{}-学生姓名-{}学生年龄-{}-所在班级:{}</p>'.format(st.id,st.s_name,st.s_age,grade.g_name)

        else:

            str += '<p>{}-学生姓名-{}学生年龄-{}-[无所在班级]</p>'.format(st.id, st.s_name, st.s_age)

    return HttpResponse(str)


def duotoduo(request):
    return render(request,'duotoduo.html')


def adduser(request):
    user = User()
    names = ['张三', '李四', '王五', '马六', '赵七', '孙八','米九']
    temp = random.randrange(0, len(names))
    user.username = names[temp] + '-' + str(random.randrange(10, 100))
    user.save()
    return HttpResponse('添加用户成功')


def addgoods(request):
    goods=Goods()
    names = ['小米', '锤子', '红米', 'oppo', '华为', '魅族', '魅蓝']
    temp = random.randrange(0, len(names))
    goods.g_name = names[temp] + '-' + str(random.randrange(10, 100))
    goods.g_price=random.randrange(100,1000)
    goods.save()
    return HttpResponse('添加商品成功')


def deletegoods(request):
    goods = Grade.objects.last()
    goods.delete()
    return HttpResponse('删除商品完成')


def deleteuser(request):
    user =User.objects.last()
    user.delete()
    return HttpResponse('删除用户完成')



# 用户添加购物车
def addcart(request):
    user =User.objects.last()
    #将最后一件商品添加到该用户的购物车中
    goods =Goods.objects.last()
    goods.g_collection.add(user)

    return HttpResponse('[ {} ] 添加 {}到购物车成功'.format(user.username,goods.g_name))


def showcart(request):
    # 一个用户 对应多个商品(购物车)
    user = User.objects.last()
    #商品列表/
    goods = user.goods_set.all()
    str = '<h1> {} 购物车 </h1>'.format(user.username)
    for i  in goods:
        str +='<p>商品名称:{},商品价格:{}</p>'.format(i.g_name,i.g_price)
    return HttpResponse(str)


def addcollect(request):
    goods = Goods.objects.last()
    user = User.objects.last()

    goods.g_collection.add(user)

    return HttpResponse('商品 {} 被 {} 收藏'.format(goods.g_name,user.username))


def showgoods(request):
    goods_list = Goods.objects.all()
    response_str = ''
    for goods  in  goods_list:
        user =goods.g_collection.all()
        response_str+= '<p>[收藏数量:{}]商品名称:{},商品价格:{}</p>'.format(user.count(),goods.g_name,goods.g_price)


    return HttpResponse(response_str)