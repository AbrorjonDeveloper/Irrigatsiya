from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticleListView.as_view(), name="articles"),
    path('<int:pk>/', ArticleDetailView.as_view(), name="article-detail"),
    path('new/', ArticlesCreateView.as_view(), name="articles_create"),
    path("<slug:slug>/update/", ArticlesUpdateView.as_view(), name="articles_update"),
    path("<slug:slug>/delete/", ArticlesDeleteView.as_view(), name="articles_delete"),
]