from django import forms
from .models import Question
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AvatarForm(forms.Form):
    image = forms.ImageField()

class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=200)
    image = forms.ImageField()

class ChoiceForm(forms.Form):
    choice_text = forms.CharField(max_length=200)
