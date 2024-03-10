from django.shortcuts import render, HttpResponse
from .models import *

def homepage(request):
    article_series = ArticleSeries.objects.all()
    context = {'objects': article_series}
    return render(request, 'myapp/home.html', context=context)

def series(request, series: str):
    articles = Article.objects.filter(series__slug=series).all()
    context = {'objects': articles}
    return render(request, 'myapp/home.html', context=context)

def article(request, series: str, article: str):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()
    context={"article": matching_article}
    return render(request=request, template_name='myapp/article.html', context=context)