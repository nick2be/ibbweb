from django.core.management.base import BaseCommand
from services.models import Service, ServiceFeature

class Command(BaseCommand):
    help = 'Force updates translation fields in the database'

    def handle(self, *args, **options):
        # Update Service translations
        for service in Service.objects.all():
            # Store current values
            current_name = service.name
            current_short_desc = service.short_description
            current_desc = service.description

            # Force update English fields
            service.name_en = current_name
            service.short_description_en = current_short_desc
            service.description_en = current_desc

            # Force update Danish fields
            service.name_da = current_name
            service.short_description_da = current_short_desc
            service.description_da = current_desc

            # Save without triggering normal save logic
            Service.objects.filter(id=service.id).update(
                name_en=current_name,
                short_description_en=current_short_desc,
                description_en=current_desc,
                name_da=current_name,
                short_description_da=current_short_desc,
                description_da=current_desc
            )
            self.stdout.write(self.style.SUCCESS(f'Updated translations for service: {service.name}'))

        # Update ServiceFeature translations
        for feature in ServiceFeature.objects.all():
            # Store current values
            current_name = feature.name
            current_desc = feature.description

            # Force update both language fields
            ServiceFeature.objects.filter(id=feature.id).update(
                name_en=current_name,
                description_en=current_desc,
                name_da=current_name,
                description_da=current_desc
            )
            self.stdout.write(self.style.SUCCESS(f'Updated translations for feature: {feature.name}')) 