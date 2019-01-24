# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context_dict = {'boldmessage': "Hello there!,Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)
    #return HttpResponse("Rango says hey there partner!"+"<br/> <a href=/rango/about/>About'</a>")

def about(request):
    context_dict={"boldmessage": "Hello there!,Kenobi,dog"}
    return render(request,"rango/about.html", context=context_dict)
