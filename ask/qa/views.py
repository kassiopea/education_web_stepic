from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, Http404
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.
from .models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.contrib.auth import login, authenticate

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
    return pagInt(request, questions, title='Новые вопросы')


def popular(request):
    questions = Question.objects.popular()
    return pagInt(request, questions, title='Популярные вопросы')

def guestionOwn(request, id):
    num = int(id)
    try:
        question = Question.objects.get(id=num)
    except Question.DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            _ = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': num})
    # answers = Answer.objects.filter(question__id=num)

    return render(request, 'question.html',
                  {'question': question,
                   'title': question.title,
                   'form': form,
                   'user': request.user,
                   'session': request.session,
                   })

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            if request.user.username != "":
                question.author = request.user
            question.save()
            return HttpResponseRedirect(url)


    else:
        form = AskForm()
    # return render(request, 'ask.html', {'form': form, })
    return render(request, 'ask.html', {'form': form,
                                        'title': 'Задать вопрос',
                                        'user': request.user,
                                        'session': request.session, })


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data["username"]
            password = form.raw_passeord
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form,
                                           'title': 'Регистрация',
                                           'user': request.user,
                                           'session': request.session, })


def loginIN(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form,
                                          'title': 'Вход в личный кабинет',
                                          'user': request.user,
                                          'session': request.session, })


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
