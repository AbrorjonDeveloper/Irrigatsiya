from django.shortcuts import render
from .models import Projects
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

class ProjectsList(ListView):
    model = Projects
    template_name = 'articles.html'
    ordering = ['-up_date']
    context_object_name = 'objects'

class ProjectsCreateView( LoginRequiredMixin , UserPassesTestMixin, CreateView):
    model = Projects
    template_name = 'articles_create.html'
    fields = ['name', 'file', 'link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
    
    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

class ProjectsUpdateView( LoginRequiredMixin , UserPassesTestMixin, UpdateView):
    model = Projects
    template_name = 'article_update.html'
    fields = ['name', 'file', 'link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
    
    def test_func(self):
        book = self.get_object()
        if book.author == self.request.user:
            return True
        return False

class ProjectsDeleteView( LoginRequiredMixin , UserPassesTestMixin, DeleteView):
    model = Projects
    template_name = 'article_delete.html'
    # fields = []

    def test_func(self):
        book = self.get_object()
        if book.author == self.request.user:
            messages.warning(self.request, "Kitob o'chirib tashlandi! ")
            return True
        return False


