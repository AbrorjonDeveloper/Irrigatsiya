from django.urls import path
from .views import BookListAPIView,BookDetailAPIView, BooksCreateView, BooksUpdateView, BooksDeleteView

urlpatterns = [
    path('', BookListAPIView.as_view(), name="books"),
    # path('', BooksList.as_view(), name="books"),
    path('<int:pk>/', BookDetailAPIView.as_view(), name="book_detail"),
    path('new/',BooksCreateView.as_view(), name="books_create"),
    path('<slug:slug>/update/',BooksUpdateView.as_view(), name="books_update"),
    path('<slug:slug>/delete/', BooksDeleteView.as_view(), name="books_delete"),
]
