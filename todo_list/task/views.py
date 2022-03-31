from django.views.generic import ListView, DetailView
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'task/home.html'
    context_object_name = 'tasks'
    context = {'title': 'Home'}


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task/details.html'
    context_object_name = 'task'

