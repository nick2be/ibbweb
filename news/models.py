from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Category(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(_('Description'), blank=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Article(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = HTMLField(_('Content'))
    excerpt = models.TextField(_('Excerpt'), max_length=200, help_text=_('A short description that will appear in article previews'))
    image = models.ImageField(_('Image'), upload_to='news/images/', blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='articles', verbose_name=_('Categories'))
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('Author'))
    published = models.BooleanField(_('Published'), default=False)
    featured = models.BooleanField(_('Featured'), default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    articles = models.ManyToManyField(Article, related_name='tags', verbose_name=_('Articles'))

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs) 