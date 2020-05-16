from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'inspiration'
urlpatterns = [
    path('poem/', views.poem_list, name='poem_list'),
    path('poem/<int:pk>/', views.poem_detail, name='poem_detail'),
    path('poem/new/', views.poem_new, name='poem_new'),
    path('poem/<int:pk>/edit/', views.poem_edit, name='poem _edit'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('edit/', views.edit, name='edit_profile'),
    path('register/', views.register, name='register'),
]