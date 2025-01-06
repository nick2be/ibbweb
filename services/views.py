from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _
from .models import Service, ServiceFeature

def service_list(request):
    services = Service.objects.all().order_by('order', 'name')
    context = {
        'services': services,
        'title': _('Our Services')
    }
    return render(request, 'services/service_list.html', context)

def service_detail(request, slug):
    service = get_object_or_404(
        Service.objects.prefetch_related('features'),
        slug=slug
    )
    related_services = Service.objects.exclude(id=service.id).order_by('name')[:3]
    context = {
        'service': service,
        'related_services': related_services,
        'title': service.name
    }
    return render(request, 'services/service_detail.html', context) 