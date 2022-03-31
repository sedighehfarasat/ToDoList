from django.views.generic import ListView
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'task/home.html'
    context_object_name = 'tasks'
