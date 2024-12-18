from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.utils.translation import get_language
from .models import Article, Category, Tag

def article_list(request):
    current_language = get_language()
    articles = Article.objects.filter(published=True).order_by('-created_at')
    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    
    context = {
        'articles': articles,
        'title': 'News & Updates'
    }
    return render(request, 'news/article_list.html', context)

def article_detail(request, slug):
    current_language = get_language()
    article = get_object_or_404(Article, slug=slug, published=True)
    
    # Get related articles based on categories and tags
    related_articles = Article.objects.filter(published=True).exclude(id=article.id)
    if article.categories.exists():
        related_articles = related_articles.filter(categories__in=article.categories.all())
    if article.tags.exists():
        related_articles = related_articles.filter(tags__in=article.tags.all())
    related_articles = related_articles.distinct().order_by(f'title_{current_language}')[:3]
    
    context = {
        'article': article,
        'related_articles': related_articles,
        'title': getattr(article, f'title_{current_language}', article.title)
    }
    return render(request, 'news/article_detail.html', context)

def category_list(request, slug):
    current_language = get_language()
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(categories=category, published=True).order_by('-created_at')
    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    
    context = {
        'category': category,
        'articles': articles,
        'title': f'Category: {getattr(category, f"name_{current_language}", category.name)}'
    }
    return render(request, 'news/category_list.html', context)

def tag_list(request, slug):
    current_language = get_language()
    tag = get_object_or_404(Tag, slug=slug)
    articles = Article.objects.filter(tags=tag, published=True).order_by('-created_at')
    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    
    context = {
        'tag': tag,
        'articles': articles,
        'title': f'Tag: {getattr(tag, f"name_{current_language}", tag.name)}'
    }
    return render(request, 'news/tag_list.html', context) 