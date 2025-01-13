from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.conf import settings
from services.models import Service
from news.models import Article

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['pages:home', 'pages:about', 'pages:privacy', 'services:list', 'contact:contact']

    def location(self, item):
        return reverse(item)

    def languages(self):
        return [lang[0] for lang in settings.LANGUAGES]

    def _urls(self, page, protocol, domain):
        urls = []
        latest_lastmod = None
        all_items = self.items()
        
        # Generate URLs for each language
        for lang_code in self.languages():
            for item in all_items:
                loc = f'/{lang_code}{self.location(item)}'
                url_info = {
                    'item': item,
                    'location': loc,
                    'lastmod': None,
                    'changefreq': self.changefreq,
                    'priority': self.priority
                }
                urls.append(url_info)
                
        return urls

class ServiceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Service.objects.filter(active=True)

    def lastmod(self, obj):
        return obj.updated_at

    def languages(self):
        return [lang[0] for lang in settings.LANGUAGES]

    def _urls(self, page, protocol, domain):
        urls = []
        all_items = self.items()
        
        for lang_code in self.languages():
            for item in all_items:
                loc = f'/{lang_code}/services/{item.slug}/'
                url_info = {
                    'item': item,
                    'location': loc,
                    'lastmod': self.lastmod(item),
                    'changefreq': self.changefreq,
                    'priority': self.priority
                }
                urls.append(url_info)
                
        return urls

class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Article.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated_at

    def languages(self):
        return [lang[0] for lang in settings.LANGUAGES]

    def _urls(self, page, protocol, domain):
        urls = []
        all_items = self.items()
        
        for lang_code in self.languages():
            for item in all_items:
                loc = f'/{lang_code}/news/{item.slug}/'
                url_info = {
                    'item': item,
                    'location': loc,
                    'lastmod': self.lastmod(item),
                    'changefreq': self.changefreq,
                    'priority': self.priority
                }
                urls.append(url_info)
                
        return urls 