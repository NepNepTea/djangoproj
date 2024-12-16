import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200, help_text = "Введите вопрос")
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to="uploads/", null=True, blank=True, help_text = "Загрузите изображение для вопроса")
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    exp_date = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=200, help_text = "Введите описание", null=True, blank=True)
    short_description = models.CharField(max_length=80, help_text = "Введите короткое описание", null=True, blank=True)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Avatar(models.Model):
    image = models.ImageField(upload_to="uploads/", null=True, blank=False)
    username = models.CharField(max_length=20)