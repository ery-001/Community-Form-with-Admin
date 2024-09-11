import django.contrib.auth
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  
    path('home', views.home, name='home'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sign-up', views.sign_up, name='sign_up'),  
    path('create_post', views.create_post, name='create_post'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
