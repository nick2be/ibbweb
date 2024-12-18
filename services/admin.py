from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import Service, ServiceFeature

class ServiceFeatureInline(TranslationTabularInline):
    model = ServiceFeature
    extra = 1

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('name', 'order', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'short_description', 'description')
    prepopulated_fields = {'slug': ('name_en',)}
    inlines = [ServiceFeatureInline]
    ordering = ('order', 'name')
    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        } 