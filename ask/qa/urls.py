from django.urls import path
from qa.views import test

urlpatterns = [
    path(r'^(\d+)/$', test, name="question-id"),
]
