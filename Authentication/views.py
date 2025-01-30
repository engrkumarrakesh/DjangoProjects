from django.shortcuts import render

# Create your views here.
def auth(request):
    return render(request, 'auth_home.html')

def login_user(request):
    return render(request, 'login.html')

def register_user(request):
    return render(request, 'register.html')