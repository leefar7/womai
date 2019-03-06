from django.conf.urls import url

from app import views

urlpatterns = [

    url(r'^index/',views.index),
    url(r'^animal/',views.animal),
    url(r'^addanimal/',views.addanimal),
    url(r'^selectanimal/',views.selectanimal),
    url(r'^deleteanimal/',views.deleteanimal),
    url(r'^updateanimal/',views.updateanimal),
    url(r'^onetoone/',views.onetoone),

    url(r'^addperson/',views.addperson),
    url(r'^bindcard/',views.bindcard),
    url(r'^deleteperson/',views.deleteperson),
    url(r'^selectcard/',views.selectcard),
    url(r'^selectperson/',views.selectperson),
    url(r'^deletecard/',views.deletecard),

    url(r'^onetoduo/', views.onetoduo),
    url(r'^addgrade/',views.addgrade),
    url(r'^addstu/',views.addstu),
    url(r'^deletegrade/',views.deletegrade),
    url(r'^deletestu/',views.deletestu),
    url(r'^selectstu/',views.selectstu),
    url(r'^selectgrade/',views.selectgrade),


    url(r'^duotoduo/',views.duotoduo),
    url(r'^adduser/',views.adduser),
    url(r'^addgoods/',views.addgoods),
    url(r'^deletegoods',views.deletegoods),
url(r'^deleteuser',views.deleteuser),

url(r'^addcart',views.addcart), #添加购物车
url(r'^showcart',views.showcart), #显示购物车
url(r'^addcollect',views.addcollect), #添加收藏
url(r'^showgoods',views.showgoods), #添加收藏



    url(r'^register/',views.register),









]
