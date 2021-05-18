from django.urls import path
from .views import *

urlpatterns = [
    path('', TodosList.as_view(), name='todos'),
    path('new/',TodosCreate.as_view(), name='todo_create'),
    
]