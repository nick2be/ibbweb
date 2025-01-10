from django import forms
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import requests
from .models import Contact, Newsletter

class ContactForm(forms.ModelForm):
    recaptcha_token = forms.CharField(widget=forms.HiddenInput(), required=True)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'company', 'subject', 'message', 'recaptcha_token']
        labels = {
            'name': _('Name'),
            'email': _('Email'),
            'company': _('Company'),
            'subject': _('Subject'),
            'message': _('Message'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Your Name')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Your Email')}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Your Company (Optional)')}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Subject')}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Your Message'), 'rows': 5}),
        }

    def clean_recaptcha_token(self):
        token = self.cleaned_data['recaptcha_token']
        if not token:
            raise forms.ValidationError(_('reCAPTCHA verification failed. Please try again.'))

        # Verify the token with Google's reCAPTCHA API
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': token
        })

        if not response.ok:
            raise forms.ValidationError(_('Failed to verify reCAPTCHA. Please try again.'))

        result = response.json()
        if not result['success']:
            raise forms.ValidationError(_('reCAPTCHA verification failed. Please try again.'))

        if result['score'] < settings.RECAPTCHA_REQUIRED_SCORE:
            raise forms.ValidationError(_('reCAPTCHA score too low. Please try again.'))

        return token

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('Enter your email address')
            })
        } 