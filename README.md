# Indicium By Bounty ApS Website

Professional website for Indicium By Bounty ApS, showcasing IT development and security services.

## Features

- Responsive design
- SEO optimized
- WCAG 2.1 AA compliant
- Secure by design
- Content management system
- Blog/News functionality

## Tech Stack

- Django 4.2.7
- PostgreSQL
- Modern frontend with responsive design
- REST API
- Whitenoise for static files

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create .env file with required environment variables:
```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/indicium
ALLOWED_HOSTS=localhost,127.0.0.1
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

## Project Structure

- `indicium/` - Main project directory
- `core/` - Core application with shared functionality
- `pages/` - Static pages and content management
- `news/` - News/blog functionality
- `services/` - Services information
- `contact/` - Contact form and handling

## Deployment

Instructions for deployment will be added here.

## Security

- HTTPS enforced
- Security headers implemented
- Regular dependency updates
- Secure form handling
- CSRF protection

## Maintenance

Instructions for content updates and maintenance will be added here. 