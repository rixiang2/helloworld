
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.db.models import Count


'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {'latest_question_list':latest_question_list,}
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


# Create your views here.
def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id);
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question, 'error_message':"You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
'''

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name='latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        #return Question.objects.order_by('-pub_date')[:5]
        print('wwwwwwwwww')
        return Question.objects.filter(pub_date__lte=timezone.now()).filter(choice__isnull=False).distinct().order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model=Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).filter(choice__isnull=False).distinct()


class ResultsView(generic.DetailView):
    model=Question
    template_name='polls/results.html'

    def get_queryset(self):
       return Question.objects.filter(pub_date__lte=timezone.now()).filter(choice__isnull=False).distinct()

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question, 'error_message':"You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))




