from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from articles.models import Articles
from books.models import Book
from presentations.models import Presentations
from django.contrib.auth.models import User


class TeacherListView(ListView):
    template_name = "teachers.html"
    model = User
    context_object_name = 'teachers'

class TeacherDetailView(DetailView):
    template_name = "teacher_detail.html"
    model = User

    def get_teacher(self):
        teacher = self.get_object_or_404(User, username=self.kwargs.get('username'))
        return teacher
    
class TeacherArticleListView(TeacherDetailView, ListView):
    model = Articles
    template_name = "teacher_articles.html"
    context_object_name = 'articles'

    def get_queryset(self):
        # teacher = get_object_or_404(User, username=self.kwargs.get('username'))
        return Articles.objects.filter(author=self.get_teacher).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['articles'] = Articles.objects.filter(author=self.get_teacher).order_by('-pub_date')
        return context 

class UserArticleListView(ListView):
    model = Articles
    template_name = 'teacher_articles.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'articles'
    # paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Articles.objects.filter(author=user).order_by('-pub_date')

class UserBooksListView(ListView):
    model = Articles
    template_name = 'teacher_articles.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'books'
    # paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Books.objects.filter(author=user).order_by('-pub_date')

class UserPresentationsListView(ListView):
    model = Presentations
    template_name = 'teacher_articles.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'presentations'
    # paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Presentations.objects.filter(author=user).order_by('-pub_date')
    


