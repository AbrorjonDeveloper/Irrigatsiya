from django.shortcuts import render
from .models import Todos
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
class TodosList(ListView):
    model = Todos
    template_name = 'todos.html'
    context_object_name = 'todos'
    ordering = ['deadline'] 

class TodosCreate(LoginRequiredMixin, CreateView ):
    model = Todos
    template_name='todo_create.html'
    fields = ['todo', 'description', 'status', 'deadline']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

        


    
