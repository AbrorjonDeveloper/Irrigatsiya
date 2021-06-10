from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/',views.categories, name='categories'),
    path('products/<int:id>/', views.products, name='product_detail'),
    path('products/',views.products, name='products'),

]