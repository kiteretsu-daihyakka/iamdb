from django.shortcuts import render,redirect
from django.contrib.auth.models import User as UserModel
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.http import FileResponse, JsonResponse
# from iamdbApp.models import AuthUser
import datetime
# Create your views here.

def loginview(request):
    if request.user.is_authenticated:
        return render(request,'logoutFst.html')

    if request.method=='POST':
        print('coming')
        username=request.POST['username']
        password=request.POST['password']
        # nwpassword=
        # user=authenticate(username=username,password=password)
        try:
            user=UserModel.objects.get(email=username,password=password)
            # ourModelusr=User.objects.get(email=email,password=password)
            # print(ourModelusr.userroleid)
            # if user is not None:
            # messages.info(request,'coming here..')
            if user.is_active:
                login(request, user)
                # ourModelusr = User.objects.get(id=userObj.id)
                # if ourModelusr.userroleid == 2:
                #     return redirect('signin:home')
                return redirect('iamdbApp:index')
            else:
                messages.info(request,'User is locked.')
        except ObjectDoesNotExist:
            messages.info(request,'Invalid Email Id or Password.')
        # return redirect('login:login')

    return render(request,'login.html',{'user':request.user})


def logoutView(request):
    logout(request)
    return redirect('authApp:login')

def frgtPwd(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'frgt.html')

def register(request):
    if request.user.is_authenticated:
        return render(request,'logoutFst.html')
    if request.method == 'POST':
        usr=UserModel(email=request.POST['email'],username=request.POST['username'],password=request.POST['password'],is_superuser=0,is_staff=0,is_active=1,date_joined=datetime.datetime.today(),first_name="foo",last_name='foo' )
        usr.save()
        login(request, usr)
        return redirect('iamdbApp:index')
    else:
        return render(request, 'register.html')

def checkUserName(request):
    if UserModel.objects.filter(username=request.GET.get('uname')).count() >= 1:
        rslt=1
    else:
        rslt = 0
    return JsonResponse(data={'rslt':rslt})

def checkEmail(request):
    if UserModel.objects.filter(email=request.GET.get('mail')).count() >= 1:
        rslt=1
    else:
        rslt = 0
    return JsonResponse(data={'rslt':rslt})
