from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import TaskForm

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['task_status'] = Task.TASK_STATUS
        filter_input = self.request.GET.get('task_status') or ''
        if filter_input:
            context['tasks'] = context['tasks'].filter(
                status=filter_input)
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"

class TaskCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = "Task was created successfully"
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(SuccessMessageMixin,LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = "Task was updated successfully"
    form_class = TaskForm

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')





