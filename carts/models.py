from django.db import models

from config import settings
from items.models import Item


class Cart(models.Model):
    items = models.ManyToManyField(
        Item,
        through='CartItem',
        related_name="items_in_cart",
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
        verbose_name='Товар'
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
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






