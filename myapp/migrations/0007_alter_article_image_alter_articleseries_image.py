# Generated by Django 5.0.3 on 2024-03-10 17:02

import myapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_article_author_article_image_articleseries_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='default/noimage.jpg', max_length=255, upload_to=myapp.models.Article.image_upload_to),
        ),
        migrations.AlterField(
            model_name='articleseries',
            name='image',
            field=models.ImageField(default='default/noimage.jpg', max_length=255, upload_to=myapp.models.ArticleSeries.image_upload_to),
        ),
    ]