from django.urls import path
from .views import ProjectsList, ProjectsCreateView, ProjectsUpdateView, ProjectsDeleteView

urlpatterns = [
    path('', ProjectsList.as_view(), name="projects"),
    path('new/',ProjectsCreateView.as_view(), name="projects_create"),
    path('<slug:slug>/update/',ProjectsUpdateView.as_view(), name="projects_update"),
    path('<slug:slug>/delete/', ProjectsDeleteView.as_view(), name="projects_delete")
]