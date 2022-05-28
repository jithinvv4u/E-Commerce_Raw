from django import forms
# from django.contrib.auth.models import User
from .models import UserData
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model=UserData
        fields=('username','first_name','last_name','email','phone','super_user','password1','password2')