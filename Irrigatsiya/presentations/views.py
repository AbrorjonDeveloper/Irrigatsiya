from django.shortcuts import render
from .models import Presentations
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

class PresentationsList(ListView):
    model = Presentations
    template_name = 'articles.html'
    ordering = ['-up_date']
    context_object_name = 'objects'

class PresentationsCreateView( LoginRequiredMixin , UserPassesTestMixin, CreateView):
    model = Presentations
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

class PresentationsUpdateView( LoginRequiredMixin , UserPassesTestMixin, UpdateView):
    model = Presentations
    template_name = 'article_update.html'
    fields = ['name', 'file', 'link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        messages.success(self.request, 'Taqdimot yangilandi!')
        return super().form_valid(form)
    
    def test_func(self):
        book = self.get_object()
        if book.author == self.request.user:
            return True
        return False

class PresentationsDeleteView( LoginRequiredMixin , UserPassesTestMixin, DeleteView):
    model = Presentations
    template_name = 'article_delete.html'
    # fields = []

    def test_func(self):
        book = self.get_object()
        if book.author == self.request.user:
            messages.warning(self.request, "Taqdimot o'chirib tashlandi! ")
            return True
        return False

