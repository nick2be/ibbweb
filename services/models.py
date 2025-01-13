from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

class Service(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.TextField(_('Short Description'), max_length=200)
    description = HTMLField(_('Description'))
    icon = models.ImageField(_('Icon'), upload_to='services/icons/')
    image = models.ImageField(_('Image'), upload_to='services/images/', blank=True, null=True)
    order = models.IntegerField(_('Order'), default=0)
    active = models.BooleanField(_('Active'), default=True, help_text=_('Enable or disable this service'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, related_name='features', on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=200)
    description = models.TextField(_('Description'))
    icon = models.CharField(_('Icon'), max_length=50, help_text=_('Font Awesome icon class'))
    order = models.IntegerField(_('Order'), default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = _('Service Feature')
        verbose_name_plural = _('Service Features')

    def __str__(self):
        return f"{self.service.name} - {self.name}" 