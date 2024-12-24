from django.core.management.base import BaseCommand
from services.models import Service
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Adds initial services to the database'

    def handle(self, *args, **kwargs):
        services = [
            {
                'name': 'Full Stack Development',
                'short_description': 'From sleek user interfaces to powerful back-end systems, our Full Stack development services deliver seamless, end-to-end solutions tailored to your business needs.',
                'description': '''Our Full Stack Development service provides comprehensive solutions that cover both front-end and back-end development. We create:

- Responsive and intuitive user interfaces
- Robust server-side applications
- RESTful APIs and microservices
- Database design and optimization
- Performance monitoring and optimization
- Security implementation and testing''',
                'order': 1,
                'icon_class': 'fas fa-layer-group'  # Represents layers/stack
            },
            {
                'name': 'Application Integrations',
                'short_description': 'Streamline your workflows and boost efficiency with our Application Integration services, connecting your systems for a seamless, unified experience.',
                'description': '''Our Application Integration services help businesses connect and streamline their various systems and applications. We offer:

- API development and integration
- Third-party system integration
- Custom middleware solutions
- Data synchronization
- Workflow automation
- Integration monitoring and maintenance''',
                'order': 2,
                'icon_class': 'fas fa-plug'  # Represents connectivity/integration
            },
            {
                'name': 'Jira Development & Administration',
                'short_description': 'Optimize your team\'s productivity with our Jira Development & Administration services—customized workflows, seamless integrations, and expert management tailored to your needs.',
                'description': '''Our Jira Development & Administration services help organizations maximize their Atlassian investment. We provide:

- Custom workflow design and implementation
- Plugin development and integration
- User management and access control
- Performance optimization
- Training and support
- Regular maintenance and updates''',
                'order': 3,
                'icon_class': 'fas fa-project-diagram'  # Represents project management/workflows
            },
            {
                'name': 'Data Visualization and Business Intelligence',
                'short_description': 'Transform your data into actionable insights with our Data Visualization and Business Intelligence solutions—empowering smarter decisions through clear, impactful visuals.',
                'description': '''Our Data Visualization and Business Intelligence services help organizations make sense of their data. We deliver:

- Interactive dashboards and reports
- Real-time data visualization
- Custom BI solutions
- Data analysis and interpretation
- KPI tracking and monitoring
- Predictive analytics integration''',
                'order': 4,
                'icon_class': 'fas fa-chart-line'  # Represents data visualization/analytics
            },
            {
                'name': 'IT Infrastructure Build and Development',
                'short_description': 'Build a robust foundation for your business with our IT Infrastructure Build and Development services—scalable, secure, and tailored to drive your success.',
                'description': '''Our IT Infrastructure Build and Development services create a solid foundation for your business operations. We provide:

- Infrastructure assessment and planning
- Cloud infrastructure setup and migration
- Network design and implementation
- Security infrastructure deployment
- Scalability planning and implementation
- Monitoring and maintenance solutions''',
                'order': 5,
                'icon_class': 'fas fa-network-wired'  # Represents IT infrastructure/networking
            },
        ]

        for service_data in services:
            service, created = Service.objects.update_or_create(
                name=service_data['name'],
                defaults={
                    'slug': slugify(service_data['name']),
                    'short_description': service_data['short_description'],
                    'description': service_data['description'],
                    'order': service_data['order']
                }
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created service "{service.name}"'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully updated service "{service.name}"')) 