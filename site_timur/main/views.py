from django.shortcuts import render
from .models import Post


def index(request):
    text = {
        'posts': Post.objects.all()
    }
    return render(request, 'main/index.html', text)


def about(request):
    return render(request, 'main/about.html', {'title': 'Мой лучшайший сайт'})
