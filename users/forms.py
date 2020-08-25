from django import forms
from django.db import models
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

#user registeration form
class UserRegisterationForm(UserCreationForm):
    email=forms.EmailField()
    username=models.CharField(max_length=100)

    REQUIRED_FIELDS = ['username', 'email' ]

    class Meta:
        model=User
        fields=['username','email','password1','password2']

# User data update form
class UserUpdateform(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']


# User profile update form (Image field)
class ProfileUpdateform (forms.ModelForm):

    class Meta:

        model=Profile

        fields=['image']


