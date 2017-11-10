from django.conf.urls import url
from tarefas.views import hello, task

urlpatterns = [
    url(r'^$', hello),
    url(r'^tarefas', task)
]