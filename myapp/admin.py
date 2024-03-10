from django.contrib import admin
from .models import *

class ArticleSeriesAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'subtitle',
        'slug',
        'published'
    ]

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Header', {'fields': ['series', 'title', 'subtitle', 'article_slug']}),
        ('Content', {'fields': ['content', 'notes']}),
        ('Date', {'fields': ['published', 'modified']})
    ]

admin.site.register(ArticleSeries, ArticleSeriesAdmin)
admin.site.register(Article, ArticleAdmin)