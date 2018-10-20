from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import loginForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'index.html',{"form":loginForm})
