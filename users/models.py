from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.CharField(
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
