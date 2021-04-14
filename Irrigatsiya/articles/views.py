from django.shortcuts import render
from .models import Articles
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .forms import ArticlesForm

class ArticlesListView(ListView):
    model = Articles
    template_name = "articles.html"
    context_object_name="objects"

class ArticlesCreateView(LoginRequiredMixin, CreateView, FormView):
    model = Articles
    template_name = "articles_create.html"
    # form_class = ArticlesForm
    fields = ['name', 'article', 'link']
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        messages.success(self.request, 'Yangi maqola ma\'lumotlar omboriga saqlab qo\'yildi!')
        return super().form_valid(form)

class ArticlesUpdateView(LoginRequiredMixin, UserPassesTestMixin,FormView, UpdateView):
    model = Articles
    template_name = "article_update.html"
    # form_class = ArticlesForm
    fields = ['name', 'article', 'link']

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Maqola yangilandi!')
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        if article.author == self.request.user:
            return True
        return False

class ArticlesDeleteView(UserPassesTestMixin, DeleteView):
    model = Articles
    template_name = "article_delete_confirm.html"
    success_url = '/articles/'

    def test_func(self):
        article = self.get_object()
        if article.author == self.request.user:
            messages.warning(self.request, "Maqola o'chirib tashlandi! ")
            return True
        return False


