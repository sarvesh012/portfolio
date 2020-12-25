from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]
    context = {'posts':posts}
    return render(request, 'base/home.html', context)

def posts(request):
    posts = Post.objects.filter(active=True)
    context = {'posts':posts}
    return render(request, 'base/posts.html', context)

def post(request, pk):
    # post = get_object_or_404(Post, id=id)
    post = Post.objects.get(id=pk)
    context = {'post':post}
    return render(request, 'base/post.html', context)

def profile(request):
    return render(request, 'base/profile.html')


