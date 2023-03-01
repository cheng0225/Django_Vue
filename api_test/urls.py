# from django.conf.urls import include
from django.urls import path
from api_test import views


app_name='api_test'
urlpatterns=[
    path('add/',views.add_things,name='add'),
    path('show/',views.show_things,name='show'),

    #这个啥 $ 好像不行 我以为是我 http api 测试有问题，还去找一堆api测试工具装   玩不明白
    # path(r'add$',views.add_things,name='add'),
    # path(r'show$',views.show_things,name='show'),
]