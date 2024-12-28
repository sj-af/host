from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as authlogin,logout as authlogout,authenticate

# Create your views here.
def login(request):
    user=None
    error_message=None
    if request.POST:
       uname=request.POST['uname']
       pword=request.POST['uname']
       print(uname,pword)
       try:
           user=User.objects.create_user(username=uname,password=pword)
       except Exception as e:
           error_message=str(e)


    return render(request,'login.html',{'user':user,'error_message':error_message})

def user_login(request):
  
    error_message=None
    if request.POST:
       uname=request.POST['uname']
       pword=request.POST['uname']
       user=authenticate(username=uname,password=pword)
       if user:
           authlogin(request,user)
           return redirect('list')
       else:
           error_message='invalid'

    return render(request,'user_login.html',{'error_message':error_message})

def logout(request):
    authlogout(request)
    return redirect('login')

