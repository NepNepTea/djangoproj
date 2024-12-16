from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AvatarForm(forms.Form):
    image = forms.ImageField()

class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=200, help_text = "Введите вопрос")
    description = forms.CharField(max_length=200, help_text = "Введите описание")
    short_description = forms.CharField(max_length=80, help_text = "Введите короткое описание")
    image = forms.ImageField(help_text = "Загрузите изображение для вопроса")

class ChoiceForm(forms.Form):
    choice_text = forms.CharField(max_length=200)
