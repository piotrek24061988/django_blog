from django.shortcuts import render


def home(request):
    return render(request, 'news_home.html')


def about(request):
    return render(request, 'about.html')
