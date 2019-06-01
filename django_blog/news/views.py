from django.shortcuts import render
from .models import Source, News


def home(request):
    context = {
        'newses': News.objects.all()
    }

    return render(request, 'news_home.html', context)


def about(request):
    return render(request, 'about.html')
