from django.urls import path
from .views import *


app_name='authApp'

urlpatterns=[
    path('',loginview,name='login'),
    path('logout/',logoutView,name='logout'),
    path('forget-password/',frgtPwd,name='frgtPwd'),
    path('register/',register,name='register'),
    path('chck-usrname/',checkUserName,name='chck_usrname'),
    path('chck-email/',checkEmail,name='chck_email'),

]