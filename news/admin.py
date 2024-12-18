from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Category, Article, Tag

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name_en',)}
    search_fields = ('name', 'description')
    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    list_display = ('title', 'author', 'published', 'featured', 'created_at', 'published_at')
    list_filter = ('published', 'featured', 'categories', 'created_at', 'published_at')
    search_fields = ('title', 'content', 'excerpt')
    prepopulated_fields = {'slug': ('title_en',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'created_at'
    filter_horizontal = ('categories', 'tags')
    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Tag)
class TagAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name_en',)}
    search_fields = ('name',)
    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        } 