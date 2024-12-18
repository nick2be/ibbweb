from modeltranslation.translator import register, TranslationOptions
from .models import Service, ServiceFeature

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description', 'description')

@register(ServiceFeature)
class ServiceFeatureTranslationOptions(TranslationOptions):
    fields = ('name', 'description') 