from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta :
        model = User
        fields = ['username','first_name','last_name', 'email']
        # Customize the labels
        labels = {'username':'Username', 'first_name':'First Name', 'last_name':'Last Name', 'email':'Email'}