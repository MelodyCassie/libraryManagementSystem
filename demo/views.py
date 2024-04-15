from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def greet(request):
    return render(request,"hello.html")


def greet_me(request, name):

    return HttpResponse(f'lets explore django, {name}',{"name":"melody"})
