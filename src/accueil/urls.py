from django.urls import path
from .views import index, article

urlpatterns = [
    path('', index, name="index-home"),
    path('article-<str:num_article>/',article,name="article-home"),
]