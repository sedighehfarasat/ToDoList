from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
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


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task/task_form.html'
    context_object_name = 'task'
    fields = '__all__'
    success_url = reverse_lazy('task-home')
