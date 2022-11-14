from django.shortcuts import render
from .models import Post





def index(request):
    posts = Post.objects.all()
    return render(request, "blog/frontend/index.html", {'posts': posts})

def about(request):
    return render(request, "blog/frontend/about.html")

def contact(request):
    return render(request, "blog/frontend/contact.html")

def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/frontend/post.html", {'post': post})

def post_details_deprecated(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/post.html", {'post': post})

def home_deprecated(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {'posts': posts})
    