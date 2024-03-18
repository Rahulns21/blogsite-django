import os
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model

class ArticleSeries(models.Model):
    class Meta:
        verbose_name_plural = 'Article Series'
        ordering = ['-published']

    def __str__(self) -> str:
        return self.title
    
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('ArticleSeries', slugify(self.slug), instance)
        return None

    image = models.ImageField(default='default/noimage.jpg', upload_to=image_upload_to, max_length=255)

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default='', blank=False)
    slug = models.SlugField('Series slug', null=False, blank=False, unique=True)
    published = models.DateTimeField("Date published", default=timezone.now)
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)

class Article(models.Model):
    class Meta:
        verbose_name_plural = 'Articles'
        ordering = ['-published']

    def __str__(self) -> str:
        return self.title
    
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('ArticleSeries', slugify(self.slug), instance)
        return None

    image = models.ImageField(default='default/noimage.jpg', upload_to=image_upload_to, max_length=255)

    series = models.ForeignKey(ArticleSeries, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default='', blank=False)
    article_slug = models.SlugField('Article slug', null=False, blank=False, unique=True)
    content = HTMLField(blank=True, default='')
    notes = HTMLField(blank=True, default='')
    published = models.DateTimeField("Date published", default=timezone.now)
    modified = models.DateTimeField("Date modified", default=timezone.now)
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)

    @property
    def slug(self):
        return self.series.slug + "/" + self.article_slug