from django.conf.urls import url
from tarefas.views import hello

urlpatterns = [
    url(r'^', hello),
]