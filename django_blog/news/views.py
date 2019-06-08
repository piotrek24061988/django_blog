from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Source, News


def home(request):
    context = {
        'newses': News.objects.all()
    }

    return render(request, 'news_home.html', context)


def about(request):
    return render(request, 'about.html')


class NewsListView(ListView):
    model = News
    template_name = 'news_home.html'
    context_object_name = 'newses'
    ordering = ['date_posted']


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_post.html'
