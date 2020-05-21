from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include, re_path
from inspiration import views

app_name = 'inspiration'
urlpatterns = [
    path('poem/', views.poem_list, name='poem_list'),
    path('poem/<int:pk>/', views.poem_detail, name='poem_detail'),
    path('poem/new/', views.poem_new, name='poem_new'),
    path('poem/<int:pk>/edit/', views.poem_edit, name='poem _edit'),
    path('poem/lovesad/', views.poem_lovesad, name='poem_lovesad'),
    #path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)