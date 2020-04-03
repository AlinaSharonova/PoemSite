from django.urls import path
from . import views

urlpatterns = [
    path('', views.poem_list, name='poem_list'),
    path('poem/<int:pk>/', views.poem_detail, name='poem_detail'),
    path('poem/new/', views.poem_new, name='poem_new'),
    path('poem/<int:pk>/edit/', views.poem_edit, name='poem _edit'),
]