import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    STATUS_CHOICES = (
        ('regular', 'Regular'),
        ('subscriber', 'Subscriber'),
        ('moderator', 'Moderator')
    )

    def __str__(self) -> str:
        return self.username

    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('Users', self.username, instance)
        return None

    image = models.ImageField(
        default='default/user.jpg', upload_to=image_upload_to)

    email = models.EmailField(unique=True)
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default='regular')
    description = models.TextField(
        'Description', max_length=600, default='', blank=True)


class SubscribedUsers(models.Model):
    class Meta:
        verbose_name_plural = 'Subscribed Users'

    def __str__(self):
        return self.email

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=200)
    created_date = models.DateTimeField('Date Created', default=timezone.now)