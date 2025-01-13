from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import Service, ServiceFeature
from django.utils.translation import gettext_lazy as _

class ServiceFeatureInline(TranslationTabularInline):
    model = ServiceFeature
    extra = 1

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('name', 'order', 'active', 'created_at', 'updated_at')
    list_filter = ('active', 'created_at', 'updated_at')
    search_fields = ('name', 'short_description', 'description')
    prepopulated_fields = {'slug': ('name_en',)}
    inlines = [ServiceFeatureInline]
    ordering = ('order', 'name')
    actions = ['make_active', 'make_inactive']
    list_editable = ['active', 'order']
    
    def make_active(self, request, queryset):
        queryset.update(active=True)
        self.message_user(request, _('Selected services have been enabled'))
    make_active.short_description = _('Enable selected services')
    
    def make_inactive(self, request, queryset):
        queryset.update(active=False)
        self.message_user(request, _('Selected services have been disabled'))
    make_inactive.short_description = _('Disable selected services')
    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        } 