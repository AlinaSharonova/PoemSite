from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from basis import views
#from basis.views import ResetPasswordRequestView, ResetPasswordView, MessageSentView

app_name = 'basis'

#router = DefaultRouter()

urlpatterns=[
    path('', views.home, name='poem_list'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileChangeView.as_view(), name='profile_edit'),
    path('logout/', views.logout_view, name='logout'),
    #path('about/', views.home, name='info'),
    #path('api/', include(router.urls)),
    #path('reset/', ResetPasswordRequestView.as_view(), name='reset_request'),
    #path('reset-password/<username>/<token>', ResetPasswordView.as_view(), name='reset'),
    #path('reset-message/', MessageSentView.as_view(), name='reset_redirect_message'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#handler500 = 'basis.views.error_500'