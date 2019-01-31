"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from qa.views import test, newQuestions, popular, guestionOwn, ask, signup, loginIN

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', newQuestions, name='main'),
    path(r'login/', loginIN, name='login'),
    path(r'signup/', signup, name='signup'),
    path(r'question/<int:id>/', guestionOwn, name='question'),
    path(r'ask/', ask, name='ask'),
    path(r'popular/', popular, name='popular'),
    path(r'new/', test, name='new'),
    # path(r'?page=', newQuestions, name='new_questions'),
]
