from django.shortcuts import render
from .models import Post, Category, Author


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'app/post_list.html', context={'posts': posts})


def post_detail(request, pk):
    post = Post.objects.filter(id=pk).first()
    return render(request, 'app/post_detail.html', context={'post': post})


def category_list(request, category):
    category_obj = Category.objects.get(name=category)
    posts = Post.objects.filter(category=category_obj)
    return render(request, 'app/category_list.html', context={'category': category_obj, 'posts': posts})