import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'indicium.settings')
django.setup()

from django.core import serializers
from django.contrib.auth.models import User
from services.models import Service, ServiceFeature
from news.models import Article, Category, Tag
from contact.models import Contact, Newsletter

def export_data():
    # Get all model instances
    services = Service.objects.all()
    features = ServiceFeature.objects.all()
    articles = Article.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    contacts = Contact.objects.all()
    newsletters = Newsletter.objects.all()
    users = User.objects.all()

    # Combine all objects
    all_objects = list(services) + list(features) + list(articles) + \
                 list(categories) + list(tags) + list(contacts) + \
                 list(newsletters) + list(users)

    # Serialize data
    with open('transfer_backup.json', 'w', encoding='utf-8') as f:
        serializers.serialize('json', all_objects, indent=2, stream=f)

def import_data():
    # Read and deserialize data
    with open('transfer_backup.json', 'r', encoding='utf-8') as f:
        objects = serializers.deserialize('json', f)
        
        # Save all objects
        for obj in objects:
            obj.save()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'import':
        import_data()
    else:
        export_data() 