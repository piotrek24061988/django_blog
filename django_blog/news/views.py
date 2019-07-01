from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Source, News
from django.http import HttpResponse, HttpResponseRedirect
from .myparser import LinksFinder


def home(request):
    context = {
        'newses': News.objects.all()
    }

    return render(request, 'news_home.html', context)


def about(request):
    return render(request, 'about.html')


def search(request):
    websites = [
        'https://www.magnapolonia.org',
        'https://www.magnapolonia.org',
        'https://wpolityce.pl',
        'https://www.tvn24.pl',
        'https://www.polsatnews.pl',
        'https://www.rt.com',
        'https://www.jpost.com',
        'https://www.washingtonpost.com',
        'https://www.aljazeera.com',
        'https://www.spiegel.de'
    ]

    source_id = {
        'https://www.magnapolonia.org': 1,
        'https://wpolityce.pl': 2,
        'https://www.tvn24.pl': 3,
        'https://www.polsatnews.pl': 3,
        'https://www.rt.com': 4,
        'https://www.jpost.com': 5,
        'https://www.washingtonpost.com': 6,
        'https://www.aljazeera.com': 7,
        'https://www.spiegel.de': 8,
    }

    words = ['polska', 'polska', 'polski', 'polskie', 'poland', 'polish', 'polnish', 'polen']
    if request.method == 'POST':
        text = request.POST.get('textfield', None)
        words = text.split()
        print(words)
        linksFinder = LinksFinder(words, websites)
        links = linksFinder.findLinks()
        print(links)
        for link, source in links.items():
            print(link, " -> ", source)
        News.objects.all().delete()
        for link, source in links.items():
            test_news = News(title=link, link=link, source_id=source_id[source])
            test_news.save()

    return HttpResponseRedirect("../")


class NewsListView(ListView):
    #model = News
    template_name = 'news_home.html'
    #context_object_name = 'newses'
    ##ordering =
    paginate_by = 5 # 5 post per page

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['newses'] = News.objects.all()
        context['sources'] = Source.objects.all()
        return context

    def get_queryset(self):
        return News.objects.order_by('name')


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
