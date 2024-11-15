from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Post
from .forms import postForm

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

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



def add_post_view(request):
    context = {}
    if request.method == "POST":
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            image = form.cleaned_data.get("image")
            description = form.cleaned_data.get("description")
            obj = Post.objects.create(title = title, image = image, description = description)
            obj.save()
            print(obj)
    else:
        form = postForm()
    context['form']= form
    return render(request, "polls/add_post.html", context)

def testing(request):
  mydata = Post.objects.all().values()
  template = loader.get_template('posts.html')
  context = {
    'myposts': mydata,
  }
  return HttpResponse(template.render(context, request))