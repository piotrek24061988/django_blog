from django.shortcuts import render


def home(request):
    return render(request, 'videos_home.html')
