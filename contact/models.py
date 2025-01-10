from django.db import models
from django.utils.translation import gettext_lazy as _

class Contact(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    email = models.EmailField(_('Email'))
    company = models.CharField(_('Company'), max_length=100, blank=True)
    subject = models.CharField(_('Subject'), max_length=200)
    message = models.TextField(_('Message'))
    recaptcha_token = models.CharField(max_length=5000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    responded = models.BooleanField(default=False)
    responded_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    unsubscribed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email 