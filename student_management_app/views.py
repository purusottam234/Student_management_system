from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def dologin(request):
    if request.method != "POST":
        return HttpResponse("Method allowed")
    else:
        return HttpResponse("Email:"+request.POST.get("email")+"password:"+request.POST.get("password"))
