from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.
from django.http import HttpResponse

from .models import Question, Answer

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def pagInt(request, questions, title):
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    paginator = Paginator(questions, 10)
    page = paginator.page(page)

    return render(request, 'questions.html',
                  {'title': title,
                   'paginator': paginator,
                   'questions': page.object_list,
                   'page': page,
                   'user': request.user,
                   'session': request.session, })

def newQuestions(request):
    questions = Question.objects.new()
    return pagInt(request, questions, title='Latest')


def popular(request):
    questions = Question.objects.popular()
    return pagInt(request, questions, title='Popular')

def guestionOwn(request, id):
    num = int(id)
    try:
        question = Question.objects.filter(id=num)

    except Question.DoesNotExist:
        raise Http404
    # answers = Answer.objects.filter(question__id=num)
    return render(request, 'question.html',
                  {'question': question,
                   # 'answers': answers,
                   'user': request.user,
                   'session': request.session, })
