# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# # Create your views here.
# def signup(request):
#     if request.method == 'POST':
#         fm = UserCreationForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#             # return redirect('signup')
#     else:
#         fm = UserCreationForm()
#     return render(request, 'signup.html', {'form':fm})



# Extended Fields SignUpForm from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, HttpResponseRedirect
from .forms import  SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here SignUpForm.
def signup(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Successfully signed up!')
            # return redirect('signup')
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form':fm})

def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data.get('username')
                upass = fm.cleaned_data.get('password')
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Successfully logged in!')
                    return HttpResponseRedirect('/authapp01/userdashboard/')
                    # return redirect('userdashboard')
        else:
            fm = AuthenticationForm()
        return render(request, 'signin.html', {'form':fm})

    else:
        return HttpResponseRedirect('/authapp01/userdashboard/')

def userdashboard(request):
    if request.user.is_authenticated:
        return render(request, 'userdashboard.html', {'username':request.user.username})
    else:
        return HttpResponseRedirect('/authapp01/signin/')

def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully logged out!')
    return HttpResponseRedirect('/authapp01/signin/')