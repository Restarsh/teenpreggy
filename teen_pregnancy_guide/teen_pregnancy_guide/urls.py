# teen_pregnancy_guide/urls.py
from django.contrib import admin
from django.urls import path
from main import views  # Import your views from the main app
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('', views.home, name='home'),  # Home page
    path('register/', views.register, name='register'),
    path('resources/', views.resources, name='resources'),
    path('consultation/', views.consultation, name='consultation'),
    path('forum/', views.forum, name='forum'),
     path('', include('main.urls')),
]
