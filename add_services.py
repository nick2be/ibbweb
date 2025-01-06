import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'indicium.settings')
django.setup()

from services.models import Service
from django.utils.text import slugify

services = [
    {
        'name_en': 'Full Stack Development',
        'name_da': 'Full Stack Udvikling',
        'short_description_en': 'End-to-end development solutions from frontend to backend.',
        'short_description_da': 'End-to-end udviklingsløsninger fra frontend til backend.',
        'description_en': 'Our full stack development services cover the entire spectrum of web and application development. From user interfaces to server architecture, we deliver complete solutions.',
        'description_da': 'Vores full stack udviklingstjenester dækker hele spektret af web- og applikationsudvikling. Fra brugergrænseflader til serverarkitektur leverer vi komplette løsninger.',
        'order': 1
    },
    {
        'name_en': 'Application Integrations',
        'name_da': 'Applikationsintegrationer',
        'short_description_en': 'Seamless integration of applications and systems.',
        'short_description_da': 'Problemfri integration af applikationer og systemer.',
        'description_en': 'We specialize in connecting different applications and systems to work together efficiently. Our integration solutions ensure smooth data flow and process automation.',
        'description_da': 'Vi er specialiserede i at forbinde forskellige applikationer og systemer til at arbejde effektivt sammen. Vores integrationsløsninger sikrer problemfri dataflow og procesautomatisering.',
        'order': 2
    },
    {
        'name_en': 'Jira Development & Administration',
        'name_da': 'Jira Udvikling & Administration',
        'short_description_en': 'Custom Jira solutions and efficient administration.',
        'short_description_da': 'Skræddersyede Jira-løsninger og effektiv administration.',
        'description_en': 'Our Jira expertise covers both custom development and administration. We help optimize your workflows and create custom solutions that match your specific needs.',
        'description_da': 'Vores Jira-ekspertise dækker både skræddersyet udvikling og administration. Vi hjælper med at optimere dine arbejdsgange og skabe tilpassede løsninger, der matcher dine specifikke behov.',
        'order': 3
    },
    {
        'name_en': 'Data Visualization and Business Intelligence',
        'name_da': 'Datavisualisering og Business Intelligence',
        'short_description_en': 'Transform data into actionable insights.',
        'short_description_da': 'Transformer data til handlingsorienterede indsigter.',
        'description_en': 'We help you make sense of your data through powerful visualization tools and business intelligence solutions. Turn complex data into clear, actionable insights.',
        'description_da': 'Vi hjælper dig med at forstå dine data gennem kraftfulde visualiseringsværktøjer og business intelligence-løsninger. Omdanner komplekse data til klare, handlingsorienterede indsigter.',
        'order': 4
    },
    {
        'name_en': 'IT Infrastructure Build and Development',
        'name_da': 'IT-infrastruktur Opbygning og Udvikling',
        'short_description_en': 'Robust and scalable IT infrastructure solutions.',
        'short_description_da': 'Robuste og skalerbare IT-infrastrukturløsninger.',
        'description_en': 'We design and implement IT infrastructure that grows with your business. Our solutions focus on security, scalability, and performance.',
        'description_da': 'Vi designer og implementerer IT-infrastruktur, der vokser med din virksomhed. Vores løsninger fokuserer på sikkerhed, skalerbarhed og ydeevne.',
        'order': 5
    }
]

for service_data in services:
    name_en = service_data['name_en']
    if not Service.objects.filter(name_en=name_en).exists():
        service = Service(
            name_en=name_en,
            name_da=service_data['name_da'],
            slug=slugify(name_en),
            short_description_en=service_data['short_description_en'],
            short_description_da=service_data['short_description_da'],
            description_en=service_data['description_en'],
            description_da=service_data['description_da'],
            order=service_data['order']
        )
        service.save()
        print(f'Added service: {name_en}') 