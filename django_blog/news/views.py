from django.shortcuts import render, get_object_or_404
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
    paginate_by = 5 # 5 post per page


class SourceNewsListView(ListView):
    model = News
    template_name = 'news_source_home.html'
    context_object_name = 'newses'
    paginate_by = 10 # 10 post per page

    def get_queryset(self):
        selected_source = get_object_or_404(Source, title=self.kwargs.get('title'))
        return News.objects.filter(source=selected_source).order_by('-date_posted')


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_post.html'
