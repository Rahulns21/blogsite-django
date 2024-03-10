from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

class ArticleSeries(models.Model):
    class Meta:
        verbose_name_plural = 'Article Series'
        ordering = ['-published']

    def __str__(self) -> str:
        return self.title

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default='', blank=False)
    slug = models.SlugField('Series slug', null=False, blank=False, unique=True)
    published = models.DateTimeField("Date published", default=timezone.now)

class Article(models.Model):
    class Meta:
        verbose_name_plural = 'Articles'
        ordering = ['-published']

    def __str__(self) -> str:
        return self.title

    series = models.ForeignKey(ArticleSeries, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default='', blank=False)
    article_slug = models.SlugField('Article slug', null=False, blank=False, unique=True)
    content = HTMLField(blank=True, default='')
    notes = HTMLField(blank=True, default='')
    published = models.DateTimeField("Date published", default=timezone.now)
    modified = models.DateTimeField("Date modified", default=timezone.now)

    @property
    def slug(self):
        return self.series.slug + "/" + self.article_slug