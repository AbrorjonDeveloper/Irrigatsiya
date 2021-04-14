from django.urls import path
from .views import EventsList, EventsCreateView, EventsUpdateView, EventsDeleteView

urlpatterns = [
    path('', EventsList.as_view(), name="events"),
    path('new/',EventsCreateView.as_view(), name="events_create"),
    path('<slug:slug>/update/',EventsUpdateView.as_view(), name="events_update"),
    path('<slug:slug>/delete/', EventsDeleteView.as_view(), name="events_delete"),
]
