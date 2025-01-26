from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse("<h1>About Page</h1>")

def contact(request):
    return HttpResponse("Contact Page")

def math(request):
    num1=10
    num2=20
    add=num1+num2
    msg="<h1>Welcomne To Math Page</h1>"
    # return HttpResponse(msg)
    return HttpResponse(add)
