from django.conf.urls import url

from elema import views

urlpatterns = [

url(r'^index/', views.index),
]