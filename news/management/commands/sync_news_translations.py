from django.core.management.base import BaseCommand
from news.models import Category, Article, Tag

class Command(BaseCommand):
    help = 'Synchronizes translation fields with default language content for news app'

    def handle(self, *args, **options):
        # Sync Category translations
        for category in Category.objects.all():
            category.name_en = category.name
            category.name_da = category.name
            category.description_en = category.description
            category.description_da = category.description
            category.save()
            self.stdout.write(self.style.SUCCESS(f'Synced translations for category: {category.name}'))

        # Sync Article translations
        for article in Article.objects.all():
            article.title_en = article.title
            article.title_da = article.title
            article.content_en = article.content
            article.content_da = article.content
            article.excerpt_en = article.excerpt
            article.excerpt_da = article.excerpt
            article.save()
            self.stdout.write(self.style.SUCCESS(f'Synced translations for article: {article.title}'))

        # Sync Tag translations
        for tag in Tag.objects.all():
            tag.name_en = tag.name
            tag.name_da = tag.name
            tag.save()
            self.stdout.write(self.style.SUCCESS(f'Synced translations for tag: {tag.name}')) 