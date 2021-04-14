from django.urls import path
from .views import VideosList, VideosCreateView, VideosUpdateView,VideosDeleteView

urlpatterns = [
    path('', VideosList.as_view(), name="videos"),
    path('new/', VideosCreateView.as_view(), name="videos_create"),
    path('<slug:slug>/update/', VideosUpdateView.as_view(), name="videos_update"),
    path('<slug:slug>/delete/', VideosDeleteView.as_view(), name="videos_delete"),
]
