from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Contact, Newsletter
from .forms import ContactForm, NewsletterForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Thank you for your message. We will get back to you soon.')
            return redirect('contact:contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'title': 'Contact Us'
    }
    return render(request, 'contact/contact.html', context)

@require_POST
def newsletter_subscribe(request):
    form = NewsletterForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        newsletter, created = Newsletter.objects.get_or_create(
            email=email,
            defaults={'active': True}
        )
        if not created and not newsletter.active:
            newsletter.active = True
            newsletter.unsubscribed_at = None
            newsletter.save()
            
        return JsonResponse({
            'status': 'success',
            'message': 'Thank you for subscribing to our newsletter!'
        })
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid email address.'
    }, status=400)

def newsletter_unsubscribe(request, email):
    try:
        newsletter = Newsletter.objects.get(email=email)
        newsletter.active = False
        newsletter.unsubscribed_at = timezone.now()
        newsletter.save()
        messages.success(request, 'You have been successfully unsubscribed from our newsletter.')
    except Newsletter.DoesNotExist:
        messages.error(request, 'Email address not found in our newsletter list.')
    
    return redirect('home') 