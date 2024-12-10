from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Question, Choice, Avatar
from django.urls import reverse
from django.views import generic
from .forms import QuestionForm, UserForm, AvatarForm, ChoiceForm
from django.contrib.auth import authenticate, login
import datetime
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'вы не сделали выбор'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def register_page(request):
    if request.method != 'POST':
        form = UserForm()
    else:
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('polls:addavatar')

    context = {'form': form}

    return render(request, 'register.html', context)



def add_variant(request, pk):
    if request.method == 'GET':
        form = ChoiceForm()
        return render(request, 'polls/choice_form.html', { 'form': form})
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            choice_text = form.cleaned_data.get("choice_text")
            question = get_object_or_404(Question, pk=pk)
            obj = Choice.objects.create(choice_text = choice_text, question = question)
            obj.save()
            return redirect('polls:index')
        else:
            return render(request, 'polls/choice_form.html', {'form': form})


def create_question_view(request):
    if request.method == 'GET':
        form = QuestionForm()
        return render(request, 'polls/question_form.html', { 'form': form})
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question_text = form.cleaned_data.get("question_text")
            image = form.cleaned_data.get("image")
            pub_date = datetime.date.today()
            author = request.user
            obj = Question.objects.create(image = image, question_text = question_text, pub_date = pub_date, author = author)
            obj.save()
            return redirect('polls:index')
        else:
            return render(request, 'polls/question_form.html', {'form': form})

def add_avatar(request):
    if request.method == 'GET':
        form = AvatarForm()
        return render(request, 'polls/add_avatar.html', { 'form': form})
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get("image")
            if request.user.is_authenticated:
                username = request.user.username
            obj = Avatar.objects.create(image = image, username = username)
            obj.save()
            return redirect('polls:index')
        else:
            return render(request, 'polls/add_avatar.html', {'form': form})

def profile_view(request):
    name = request.user.username
    if Avatar.objects.filter(username=name):
        avatar = Avatar.objects.get(username=name)
    else:
        avatar = Avatar.objects.get(username='default')
    email = request.user.email
    return render(request,'polls/profile.html', context={'avatar': avatar, 'email': email, 'name':name},)

def change_img(request, pk):
    if request.method == 'GET':
        form = AvatarForm()
        return render(request, 'polls/change_avatar.html', { 'form': form})
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get("image")
            avatar = get_object_or_404(Avatar, pk=pk)
            avatar.image=image
            avatar.save()
            return redirect('polls:profile')
        else:
            return render(request, 'polls/change_avatar.html', {'form': form})

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("polls:index")