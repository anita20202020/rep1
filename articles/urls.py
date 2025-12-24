# articles/urls.py
from django.urls import path
from .views import (
    article_list,
    article_create,
    article_edit,
    article_delete,
    api_articles,
    api_article_detail,
)

urlpatterns = [

    path('', article_list, name='article_list'),
    path('create/', article_create, name='article_create'),
    path('<int:id>/edit/', article_edit, name='article_edit'),
    path('<int:id>/delete/', article_delete, name='article_delete'),
    

    path('api/articles/', api_articles, name='api_articles'),
    path('api/articles/<int:pk>/', api_article_detail, name='api_article_detail'),
]