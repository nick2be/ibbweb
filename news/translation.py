from modeltranslation.translator import register, TranslationOptions
from .models import Article, Category, Tag

@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'excerpt')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',) 