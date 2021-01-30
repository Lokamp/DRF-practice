from django.db import models

from config import settings
from items.models import Item


class Cart(models.Model):
    items = models.ManyToManyField(
        Item,
        through='CartItem'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="users",
        verbose_name='Пользователь'
    )


class CartItem(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name='Пользователь'
    )
    cart = models.ForeignKey(
        to=Cart,
        on_delete=models.CASCADE,
        related_name="carts",
        verbose_name='Корзина'
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )






