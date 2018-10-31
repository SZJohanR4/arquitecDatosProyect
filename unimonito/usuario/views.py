from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import loginForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User


def index(request):
    return render(request,'index.html',{"form":loginForm})


def login(request):
    login=loginForm(request.POST or None)
    if login.is_valid():
        datos=login.cleaned_data
        username =datos.get("user_name")
        password =datos.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            print(user.is_superuser)
            return HttpResponseRedirect('/index')
            #return render(request,'index.html',{"sesion":user})
        else:
            fail="Datos Incorrectos"
            return render(request,'index.html',{"form":login, "fail":fail})
    return render(request,'index.html',{"form":login})
