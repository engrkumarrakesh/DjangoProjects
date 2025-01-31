from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

# SignUp form Inharited from UserCreationForm
class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta :
        model = User
        fields = ['username','first_name','last_name', 'email']
        # Customize the labels
        labels = {'username':'Username', 'first_name':'First Name', 'last_name':'Last Name', 'email':'Email'}

        


# UserChange form Inharited from UserChangeForm

class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email','date_joined','last_login']
        labels = {'username':'Username', 'first_name':'First Name', 'last_name':'Last Name', 'email':'Email', 'date_joined':'Date Joined', 'last_login':'Last Login'}


class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        labels = {'username':'Username', 'first_name':'First Name', 'last_name':'Last Name', 'email':'Email', 'date_joined':'Date Joined', 'last_login':'Last Login'}
     