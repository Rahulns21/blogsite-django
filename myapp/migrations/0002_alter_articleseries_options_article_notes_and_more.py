# Generated by Django 5.0.3 on 2024-03-07 16:35

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articleseries',
            options={'ordering': ['-published'], 'verbose_name_plural': 'Article Series'},
        ),
        migrations.AddField(
            model_name='article',
            name='notes',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='articleseries',
            name='subtitle',
            field=models.CharField(default='', max_length=200),
        ),
    ]
