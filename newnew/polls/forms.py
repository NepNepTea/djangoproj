from django import forms
from .models import Question
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class HotelForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']