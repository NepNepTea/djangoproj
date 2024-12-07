from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from polls.models import Avatar


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AvatarForm(UserCreationForm):
    class Meta:
        model = Avatar
        fields = ['image']