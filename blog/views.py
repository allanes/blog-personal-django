from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {'posts': posts})
    

def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/post.html", {'post': post})
