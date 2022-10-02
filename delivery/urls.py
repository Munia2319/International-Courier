from django.urls import path
from . import views
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from delivery import views
from django.urls import include, path
from rest_framework import routers


app_name='delivery'

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('home/', views.home_page, name="home"),
    path('second/',views.second_page, name='second_page' ),
    path('third/',views.third_page, name='third' ),
    path('test/',views.test_page, name='test' ),
    path('api_view/',views.api_view),
    path('pending_delivery/',views.pending_delivery,name="pending_delivery"),
    path('completed_delivery/',views.completed_delivery,name="completed_delivery"),
    path('pending_payment/',views.pending_payment,name="pending_payment"),
    path('test_payment/',views.return_api,name="return_api"),
    path('payment_success/',views.success_payment,name="success_payment"),
    #path('save_page/',views.save_page,name="save_page"),
    #path('keycloack/',views.login,name='login'),
    

    

    ]