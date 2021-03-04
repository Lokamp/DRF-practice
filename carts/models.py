from django.db import models

from config import settings
from items.models import Item


class Cart(models.Model):
    items = models.ManyToManyField(
        Item,
        through='CartItem',
        related_name="carts",
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
        verbose_name='Товар',
        related_name='cart_items'
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        verbose_name='Корзина',
        related_name='cart_items'
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
        blank=True,
        null=True
    )

    @property
    def total_price(self):
        return self.quantity * self.price
