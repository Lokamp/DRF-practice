from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from config import settings


class User(AbstractUser):
    email = models.EmailField(
        max_length=255,
        verbose_name='Email адрес'
    )
    middle_name = models.CharField(
        max_length=120,
        verbose_name='Отчество'
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name='Номер телефона'
    )
    address = models.CharField(
        max_length=120,
        verbose_name='Адрес'
    )
    premium = models.BooleanField(
        default=False,
        verbose_name='Статус пользователя'
    )

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
