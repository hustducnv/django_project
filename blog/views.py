from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Ducnv',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'July 17, 2020'
    },
    {
        'author': 'Longnv',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'July 18, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)