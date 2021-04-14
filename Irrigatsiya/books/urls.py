from django.urls import path
from .views import BooksList, BooksCreateView, BooksUpdateView, BooksDeleteView

urlpatterns = [
    path('', BooksList.as_view(), name="books"),
    path('new/',BooksCreateView.as_view(), name="books_create"),
    path('<slug:slug>/update/',BooksUpdateView.as_view(), name="books_update"),
    path('<slug:slug>/delete/', BooksDeleteView.as_view(), name="books_delete"),
]
