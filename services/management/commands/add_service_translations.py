from django.core.management.base import BaseCommand
from services.models import Service

class Command(BaseCommand):
    help = 'Adds Danish translations for services'

    def handle(self, *args, **kwargs):
        translations = {
            'Full Stack Development': {
                'name_da': 'Full Stack Udvikling',
                'short_description_da': 'Fra elegante brugergrænseflader til kraftfulde backend-systemer leverer vores Full Stack-udviklingstjenester sømløse, komplette løsninger skræddersyet til dine forretningsbehov.',
                'description_da': '''Vores Full Stack-udviklingstjeneste leverer omfattende løsninger, der dækker både frontend- og backend-udvikling. Vi skaber:

- Responsive og intuitive brugergrænseflader
- Robuste server-side applikationer
- RESTful API'er og mikroservices
- Database design og optimering
- Ydelses-overvågning og optimering
- Sikkerhedsimplementering og test'''
            },
            'Application Integrations': {
                'name_da': 'Applikationsintegrationer',
                'short_description_da': 'Strømlin dine arbejdsgange og øg effektiviteten med vores Applikationsintegrationstjenester, der forbinder dine systemer for en sømløs, samlet oplevelse.',
                'description_da': '''Vores Applikationsintegrationstjenester hjælper virksomheder med at forbinde og strømline deres forskellige systemer og applikationer. Vi tilbyder:

- API-udvikling og integration
- Tredjepartssystem-integration
- Skræddersyede middleware-løsninger
- Datasynkronisering
- Workflow-automatisering
- Integrationsovervågning og vedligeholdelse'''
            },
            'Jira Development & Administration': {
                'name_da': 'Jira Udvikling & Administration',
                'short_description_da': 'Optimer dit teams produktivitet med vores Jira Udviklings- & Administrationstjenester—tilpassede arbejdsgange, sømløse integrationer og ekspert administration skræddersyet til dine behov.',
                'description_da': '''Vores Jira Udviklings- & Administrationstjenester hjælper organisationer med at maksimere deres Atlassian-investering. Vi leverer:

- Tilpasset workflow design og implementering
- Plugin-udvikling og integration
- Brugerstyring og adgangskontrol
- Ydelsesoptimering
- Træning og support
- Regelmæssig vedligeholdelse og opdateringer'''
            },
            'Data Visualization and Business Intelligence': {
                'name_da': 'Datavisualisering og Business Intelligence',
                'short_description_da': 'Transformer dine data til handlingsorienterede indsigter med vores Datavisualisering og Business Intelligence-løsninger—gør det muligt at træffe smartere beslutninger gennem klare, effektfulde visualiseringer.',
                'description_da': '''Vores Datavisualisering og Business Intelligence-tjenester hjælper organisationer med at få mening ud af deres data. Vi leverer:

- Interaktive dashboards og rapporter
- Realtids datavisualisering
- Skræddersyede BI-løsninger
- Dataanalyse og fortolkning
- KPI-sporing og overvågning
- Integration af forudsigende analyser'''
            },
            'IT Infrastructure Build and Development': {
                'name_da': 'IT-infrastruktur Opbygning og Udvikling',
                'short_description_da': 'Byg et robust fundament for din virksomhed med vores IT-infrastruktur Opbygnings- og Udviklingstjenester—skalerbar, sikker og skræddersyet til at drive din succes.',
                'description_da': '''Vores IT-infrastruktur Opbygnings- og Udviklingstjenester skaber et solidt fundament for din virksomhedsdrift. Vi leverer:

- Infrastrukturvurdering og planlægning
- Cloud-infrastruktur opsætning og migrering
- Netværksdesign og implementering
- Sikkerhedsinfrastruktur implementering
- Skalerbarhedsplanlægning og implementering
- Overvågnings- og vedligeholdelsesløsninger'''
            }
        }

        for service in Service.objects.all():
            if service.name in translations:
                trans = translations[service.name]
                for field, value in trans.items():
                    setattr(service, field, value)
                service.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully added Danish translations for "{service.name}"'))
            else:
                self.stdout.write(self.style.WARNING(f'No translations found for "{service.name}"')) 