from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
    text = """<h1>hello ,Welcome to my First Django app"""
    return HttpResponse(text);
