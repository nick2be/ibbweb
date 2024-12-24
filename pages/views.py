from django.shortcuts import render
from django.views.generic import TemplateView
from services.models import Service
from news.models import Article
from django.utils.translation import activate, gettext as _, get_language
from django.http import HttpResponse

def home(request):
    current_language = get_language()
    services = Service.objects.all().order_by('order', f'name_{current_language}')[:6]
    latest_news = Article.objects.filter(published=True).order_by('-created_at')[:2]
    context = {
        'services': services,
        'latest_news': latest_news,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    context = {
        'title': _('About Us'),
        'years_experience': 9,
    }
    return render(request, 'pages/about.html', context)

def privacy(request):
    return render(request, 'pages/privacy.html', {'title': _('Privacy Policy')})

def test_danish(request):
    activate('da')
    return HttpResponse(_('Home'), content_type='text/plain') 