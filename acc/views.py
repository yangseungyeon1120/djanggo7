from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .models import User

def chpass(request):
    cp = request.POST.get("cpass")
    np = request.POST.get("npass")
    if check_password(cp, u.password):
        np=request.POST.get("npass")
        u.set_password(np)
        u.save()
        return redirect("acc:login")
    return redirect("acc:update")
       


def update(request):
    if request.method == "POST":
        u = request.user
        up = request.POST.get("upass")
        uc = request.POST.get("ucomm")
        ue = request.POST.get("umail")
        uf = request.POST.get("fname")
        ul = request.POST.get("lanme")
        pi = request.POST.get("upic")
        if pi:
            u.pic.delete()
            u.pic=pi
        u.comment, u.email, u.first_name, u.last_name = uc, ue, uf, ul
        u.save()
    return render(request, "acc/update.html")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        uc = request.POST.get("ucomm")
        ue = request.POST.get("umail")
        uf = request.POST.get("fname")
        ul = request.POST.get("lanme")
        pi = request.POST.get("upic")
       User.objects.create_user(username=un, password=up, comment=uc, email=ue, first_name=uf, last_name=ul, pic=pi)
        return redirect("acc:login")
    return render(request, "acc/singup.html")

def delete(request):
    cp = request.post.get("cpass")
    if check_passod(cp, u.password):
        u.pic.delete()
        u.delete()
        return redirect("acc:index")
    else:
        pass
   
    return redirect("acc:profile")

def profile(request):
    return render(request, "acc/profile.html")


def userlogout(request):
    logout(request)
    return render(request, "acc/index.html")


def userlogin(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u :
            login(request, u)
            return redirect("acc:index")
        else:
            pass
    return render(request, "acc/login.html")




def index(request):
    return render(request, "acc/index.html")