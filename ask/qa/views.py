from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.
from django.http import HttpResponse

from .models import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def newQuestions(request):
    questions = Question.objects.new()

    limit = request.GET.get('limit', 10)
    try:
        page = request.GET.get('page', 1)
    except ValueError:
        raise Http404
        paginator = Paginator(questions, limit)
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, 'new_questions.html', {
    'questions': page.object_list,
    'paginator': paginator, 'page': page,
    })

# def paginate(request, qs):
#     try:
#         limit = int(request.GET.get('limit', 10))
#     except ValueError:
#         limit = 10
#         if limit > 100:
#             limit = 10
#             try:
#                 page = int(request.GET.get('page', 1))
#             except ValueError:
#                 raise Http404
#                 paginator = Paginator(qs, limit)
#                 try:
#                     page = paginator.page(page)
#                 except EmptyPage:
#                     page = paginator.page(paginator.num_pages)
#                     return page
