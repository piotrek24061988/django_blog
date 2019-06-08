from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog_home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog_home.html'
    context_object_name = 'posts'
    ordering = ['date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_post.html'


class PostCreateView(DetailView):
    model = Post
    template_name = 'blog_post.html'