from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('category/<slug:slug>/', views.category_list, name='category'),
    path('tag/<slug:slug>/', views.tag_list, name='tag'),
    path('<slug:slug>/', views.article_detail, name='detail'),
] 