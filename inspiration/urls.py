from django.urls import path
from . import views

urlpatterns = [
    path('', views.poem_list, name='poem_list'),
    path('poem/<int:pk>/', views.poem_detail, name='poem_detail'),
]