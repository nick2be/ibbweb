from django.core.management.base import BaseCommand
from services.models import Service, ServiceFeature

class Command(BaseCommand):
    help = 'Synchronizes translation fields with default language content'

    def handle(self, *args, **options):
        # Sync Service translations
        for service in Service.objects.all():
            service.name_en = service.name
            service.name_da = service.name
            service.short_description_en = service.short_description
            service.short_description_da = service.short_description
            service.description_en = service.description
            service.description_da = service.description
            service.save()
            self.stdout.write(self.style.SUCCESS(f'Synced translations for service: {service.name}'))

        # Sync ServiceFeature translations
        for feature in ServiceFeature.objects.all():
            feature.name_en = feature.name
            feature.name_da = feature.name
            feature.description_en = feature.description
            feature.description_da = feature.description
            feature.save()
            self.stdout.write(self.style.SUCCESS(f'Synced translations for feature: {feature.name}')) 