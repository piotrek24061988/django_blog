from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='news-home'),
    path('post/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('', views.NewsListView.as_view(), name='news-home'),
    path('about/', views.about, name='news-about'),
]
