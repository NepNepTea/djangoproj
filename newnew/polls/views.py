from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import HotelForm, UserForm

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
            form.save()
            return redirect('polls:index')

    context = {'form': form}

    return render(request, 'register.html', context)


class ChoiceCreateView(CreateView):
    model = Choice
    fields = '__all__'

def create_question_view(request):

    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('polls:createchoice')
    else:
        form = HotelForm()
    return render(request, 'polls/question_form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')