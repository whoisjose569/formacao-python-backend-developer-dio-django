from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


def authenticate_user(request):
    context = {}
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("contacts:create"))
        else:
            context["message"] = "Usuario ou senha invalidos!"
            return render(request, "accounts/login.html", context)

    return render(request, "accounts/login.html", context)

def loggout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("accounts:login"))