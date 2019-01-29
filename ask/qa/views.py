from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.
from django.http import HttpResponse

from .models import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def pagInt(request):
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    return page

def newQuestions(request):
    page = pagInt(request)

    questions = Question.objects.new()
    paginator = Paginator(questions, 10)

    page = paginator.page(page)

    return render(request, 'new_questions.html',
                  {'title': 'Latest',
                   'paginator': paginator,
                   'questions': page.object_list,
                   'page': page,
                   'user': request.user,
                   'session': request.session, })

# def popular(request):
#     try:
#         page = int(request.GET.get("page"))
#     except ValueError:
#         page = 1
#     except TypeError:
#         page = 1
