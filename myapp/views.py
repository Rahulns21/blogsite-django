import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from uuid import uuid4
from .decorators import *
from .models import *
from .forms import *
from django.core.mail import EmailMessage
from users.models import SubscribedUsers
from .forms import NewsletterForm

def homepage(request):
    article_series = ArticleSeries.objects.all()
    context = {'objects': article_series, 'type': 'series'}
    return render(request, 'myapp/home.html', context=context)


def series(request, series: str):
    articles = Article.objects.filter(series__slug=series).all()
    context = {'objects': articles, 'type': 'article'}
    return render(request, 'myapp/home.html', context=context)


def article(request, series: str, article: str):
    matching_article = Article.objects.filter(
        series__slug=series, article_slug=article).first()
    context = {"article": matching_article}
    return render(request, 'myapp/article.html', context=context)


@user_is_superuser
def new_series(request):
    if request.method == 'POST':
        form = SeriesCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:homepage')
    else:
        form = SeriesCreateForm()

    context = {'object': 'Series', 'form': form}
    return render(request, 'myapp/new_record.html', context=context)


@user_is_superuser
def new_post(request):
    if request.method == 'POST':
        form = ArticleCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f"{form.cleaned_data['series'].slug}/{form.cleaned_data.get('article_slug')}")
    else:
        form = ArticleCreateForm()

    context = {'object': 'Article', 'form': form}
    return render(request, 'myapp/new_record.html', context=context)


@user_is_superuser
def series_update(request, series):
    matching_series = ArticleSeries.objects.filter(slug=series).first()

    if request.method == "POST":
        form = SeriesUpdateForm(request.POST, request.FILES, instance=matching_series)
        if form.is_valid():
            form.save()
            return redirect('myapp:homepage')
    else:
        form = SeriesUpdateForm(instance=matching_series)

        context={"object": "Series", "form": form}
        return render(request, 'myapp/new_record.html', context=context)


@user_is_superuser
def series_delete(request, series):
    matching_series = ArticleSeries.objects.filter(slug=series).first()

    if request.method == "POST":
        matching_series.delete()
        return redirect('/')
    else:
        context={"object": matching_series, "type": "Series"}
        return render(request, 'myapp/confirm_delete.html', context=context)


@user_is_superuser
def article_update(request, series, article):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()

    if request.method == "POST":
        form = ArticleUpdateForm(request.POST, request.FILES, instance=matching_article)
        if form.is_valid():
            form.save()
            return redirect(f'/{matching_article.slug}')
    else:
        form = ArticleUpdateForm(instance=matching_article)

        context={"object": "Article", "form": form}
        return render(request, 'myapp/new_record.html', context=context)


@user_is_superuser
def article_delete(request, series, article):
    matching_article = Article.objects.filter(
        series__slug=series, article_slug=article).first()

    if request.method == 'POST':
        matching_article.delete()
        return redirect('/')
    else:
        context = {'object': matching_article, 'type': 'article'}
        return render(request, 'myapp/confirm_delete.html', context=context)
    
@csrf_exempt
@user_is_superuser
def upload_image(request, series: str=None, article: str=None):
    if request.method != "POST":
        return JsonResponse({'Error Message': "Wrong request"})

    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()
    if not matching_article:
        return JsonResponse({'Error Message': f"Wrong series ({series}) or article ({article})"})

    file_obj = request.FILES['file']
    file_name_suffix = file_obj.name.split(".")[-1]
    if file_name_suffix not in ["jpg", "png", "gif", "jpeg"]:
        return JsonResponse({"Error Message": f"Wrong file suffix ({file_name_suffix}), image types supported are .jpg, .png, .gif, .jpeg"})

    file_directory = os.path.join(settings.MEDIA_ROOT, 'ArticleSeries', matching_article.slug)
    if not os.path.exists(file_directory):
        os.makedirs(file_directory)

    file_path = os.path.join(file_directory, file_obj.name)
    if os.path.exists(file_path):
        file_obj.name = str(uuid4()) + '.' + file_name_suffix
        file_path = os.path.join(file_directory, file_obj.name)

    with open(file_path, 'wb+') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)

    return JsonResponse({
        'message': 'Image uploaded successfully',
        'location': os.path.join(settings.MEDIA_URL, 'ArticleSeries', matching_article.slug, file_obj.name)
    })

@user_is_superuser
def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')

            mail = EmailMessage(subject, email_message, f"PyLessons <{request.user.email}>", bcc=receivers)
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request, "Email sent succesfully")
            else:
                messages.error(request, "There was an error sending email")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('/')

    form = NewsletterForm()
    form.fields['receivers'].initial = ','.join([active.email for active in SubscribedUsers.objects.all()])
    return render(request=request, template_name='myapp/newsletter.html', context={'form': form})