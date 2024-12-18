from django.contrib import admin
from .models import Contact, Newsletter

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'read', 'responded')
    list_filter = ('read', 'responded', 'created_at')
    search_fields = ('name', 'email', 'company', 'subject', 'message')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'active')
    list_filter = ('active', 'subscribed_at')
    search_fields = ('email',)
    readonly_fields = ('subscribed_at', 'unsubscribed_at') 