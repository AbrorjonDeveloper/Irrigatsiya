from django.urls import path
from .views import PresentationsList, PresentationsCreateView, PresentationsUpdateView, PresentationsDeleteView

urlpatterns = [
    path('', PresentationsList.as_view(), name="presentations"),
    path('new/',PresentationsCreateView.as_view(), name="presentations_create"),
    path('<slug:slug>/update/',PresentationsUpdateView.as_view(), name="presentations_update"),
    path('<slug:slug>/delete/', PresentationsDeleteView.as_view(), name="presentations_delete"),
]
