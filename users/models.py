from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=120, unique=True
    )
    password = models.CharField(
        max_length=120
    )
    email = models.CharField(
        max_length=255
    )
    first_name = models.CharField(
        max_length=120
    )
    last_name = models.CharField(
        max_length=120
    )
    middle_name = models.CharField(
        max_length=120
    )
    phone_number = models.CharField(
        max_length=20
    )
    address = models.CharField(
        max_length=120
    )
    premium = models.BooleanField(
        default=False
    )
