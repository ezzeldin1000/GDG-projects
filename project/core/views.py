# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("welcome to home page")

def about(request):
    return HttpResponse("welcome to about page")