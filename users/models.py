from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    STATUS_CHOICES = (
        ('regular', 'Regular'),
        ('subscriber', 'Subscriber'),
        ('moderator', 'Moderator')
    )

    def __str__(self) -> str:
        return self.username

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='regular')
    description = models.TextField('Description', max_length=600, default='', blank=True)
