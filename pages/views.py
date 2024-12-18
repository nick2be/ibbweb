from django.shortcuts import render
from django.views.generic import TemplateView
from services.models import Service
from news.models import Article

def home(request):
    services = Service.objects.all()[:6]
    latest_news = Article.objects.filter(published=True).order_by('-created_at')[:2]
    context = {
        'services': services,
        'latest_news': latest_news,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    context = {
        'title': 'About Us',
        'years_experience': 9,
    }
    return render(request, 'pages/about.html', context)

def privacy(request):
    return render(request, 'pages/privacy.html', {'title': 'Privacy Policy'}) 