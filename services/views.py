from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language
from django.db.models import Prefetch
from .models import Service, ServiceFeature

def service_list(request):
    current_language = get_language()
    services = Service.objects.all().order_by('order', f'name_{current_language}')
    context = {
        'services': services,
        'title': 'Our Services'
    }
    return render(request, 'services/service_list.html', context)

def service_detail(request, slug):
    current_language = get_language()
    service = get_object_or_404(
        Service.objects.prefetch_related(
            Prefetch(
                'features',
                queryset=ServiceFeature.objects.all().order_by('order', f'name_{current_language}')
            )
        ),
        slug=slug
    )
    related_services = Service.objects.exclude(id=service.id).order_by(f'name_{current_language}')[:3]
    context = {
        'service': service,
        'related_services': related_services,
        'title': getattr(service, f'name_{current_language}', service.name)
    }
    return render(request, 'services/service_detail.html', context) 