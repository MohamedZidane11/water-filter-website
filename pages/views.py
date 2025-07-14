from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1 style='background-color:powderblue';>Hello world</h1>")
