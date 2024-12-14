# teen_pregnancy_guide/urls.py
from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('register/', views.register, name='register'),
    path('resources/', views.resources, name='resources'),
    path('consultation/', views.consultation, name='consultation'),
    path('forum/', views.forum, name='forum'),
]
