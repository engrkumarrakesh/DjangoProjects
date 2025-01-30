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
from django.shortcuts import render
from .forms import  SignUpForm
from django.contrib import messages
# Create your views here.
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