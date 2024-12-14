# main/views.py
from django.shortcuts import render, redirect
from .models import Resource, ForumPost
from .forms import RegistrationForm

# Home Page View
def home(request):
    resources = Resource.objects.all()
    return render(request, 'home.html', {'resources': resources})

# Register View (for registration page)
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user
            return redirect('home')  # Redirect to home after successful registration
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})

# Resources View
def resources(request):
    resources = Resource.objects.all()
    return render(request, 'resources.html', {'resources': resources})

# Consultation View
def consultation(request):
    return render(request, 'consultation.html')

# Forum View
def forum(request):
    posts = ForumPost.objects.all()
    return render(request, 'forum.html', {'posts': posts})
