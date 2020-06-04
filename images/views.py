from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Image, Comment, Like
from .forms import PostForm, ProfileUploadForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.objects.all()
    print(images)
    return render(request, 'index.html', {"images":images})


