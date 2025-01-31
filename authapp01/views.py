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
from .forms import  SignUpForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User

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



# # 1 User Dashboard without Admin and User Filter Specific Dashboard
# def userdashboard(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             fm = EditUserProfileForm(request.POST, instance=request.user)
#             if fm.is_valid():
#                 fm.save()
#                 messages.success(request, 'Profile updated successfully!')
#                 return HttpResponseRedirect('/authapp01/userdashboard/')
#         else:
#             fm = EditUserProfileForm(instance=request.user)
#         # fm = UserChangeForm(instance=request.user)  # for default 
#         fm = EditUserProfileForm(instance=request.user) 
#         return render(request, 'userdashboard.html', {'username':request.user.username, 'form':fm})
#     else:
#         return HttpResponseRedirect('/authapp01/signin/')

# 2 User Dashboard with Admin and User Filter Specific Dashboard
# def userdashboard(request):
#     if request.user.is_authenticated:
#         #POST Request
#         if request.method == 'POST':
#             if request.user.is_superuser==True:
#                 fm=EditAdminProfileForm(request.POST, instance=request.user)
#             else:
#                 fm=EditUserProfileForm(request.POST, instance=request.user)
#             if fm.is_valid():
#                 fm.save()
#                 messages.success(request, 'Profile updated successfully!')
#                 return HttpResponseRedirect('/authapp01/userdashboard/')
        
#         #GET Request
#         else:
#             if request.user.is_superuser==True:
#                  fm=EditAdminProfileForm(instance=request.user)
#             else:
#                 fm=EditUserProfileForm(instance=request.user)
#             return render(request, 'userdashboard.html', {'username':request.user.username, 'form':fm})
#     else:
#         return HttpResponseRedirect('/authapp01/signin/')

# 3 User Dashboard with Admin and User Filter Specific Dashboard and Fatching users list in admin dashboard using Model
def userdashboard(request):
    if request.user.is_authenticated:
        #POST Request
        if request.method == 'POST':

            if request.user.is_superuser==True:
                fm=EditAdminProfileForm(request.POST, instance=request.user)
                user= User.objects.all() #pass model entity to html
            else:
                fm=EditUserProfileForm(request.POST, instance=request.user)
                user=None
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Profile updated successfully!')
                return HttpResponseRedirect('/authapp01/userdashboard/')
        
        #GET Request
        else:
            if request.user.is_superuser==True:
                 fm=EditAdminProfileForm(instance=request.user)
                 user= User.objects.all() #pass model entity to html
            else:
                fm=EditUserProfileForm(instance=request.user)
                user=None
            return render(request, 'userdashboard.html', {'username':request.user.username, 'form':fm, 'user':user})

    else:
        return HttpResponseRedirect('/authapp01/signin/')

# Logout Functions
def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully logged out!')
    return HttpResponseRedirect('/authapp01/signin/')




#Change Password with old password and new password
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                # Save the new password
                # new_password = fm.cleaned_data.get('new_password')
                # user = request.user
                # user.set_password(new_password)
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password changed successfully!')
                return HttpResponseRedirect('/authapp01/userdashboard/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'change_password.html', {'form':fm})
    else:
        return HttpResponseRedirect('/authapp01/signin/')




# Change Password without old password and new password
def change_password_without_old_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password changed successfully!')
                return HttpResponseRedirect('/authapp01/userdashboard/')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'changepass_without_old.html', {'form':fm})
    else:
        return HttpResponseRedirect('/authapp01/signin/')

# User Details
def userdetails(request, id):
    if request.user.is_authenticated:
        pi=User.objects.get(pk=id)
        fm=EditAdminProfileForm(instance=pi)
        return render(request, 'userdetails.html', {'form':fm})
    else:
        return HttpResponseRedirect('/authapp01/signin/')