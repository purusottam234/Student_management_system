from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login as dj_login, logout
from student_management_app.EmailBackEnd import EmailBackEnd


# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def dologin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get(
            "email"), password=request.POST.get("password"))
        if user != None:
            dj_login(request, user)
            return HttpResponse("Email:"+request.POST.get("email")+"password:"+request.POST.get("password"))
        else:
            return HttpResponse('invalid login')


def GetUserDetails(request):
    if request.user != None:
        return HttpResponse('user:'+request.user.email+'usertype:'+str(request.user.user_type))
    else:
        return HttpResponse("please login first")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
