from django.urls import path
from .views import *
urlpatterns = [
    path("<int:pk>/", TeacherDetailView.as_view(), name="teacher_detail"),
    path("<int:pk>/articles/", TeacherArticleListView.as_view(), name="teacher_articles"),
    path('<str:username>-articles',UserArticleListView.as_view(), name="user_articles"),
]
