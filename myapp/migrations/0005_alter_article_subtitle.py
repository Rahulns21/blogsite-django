# Generated by Django 5.0.3 on 2024-03-08 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_article_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='subtitle',
            field=models.CharField(default='', max_length=200),
        ),
    ]
