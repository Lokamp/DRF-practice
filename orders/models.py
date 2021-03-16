from django.db import models

from carts.models import Cart
from config import settings
from items.models import Item


class Order(models.Model):
    class OrderStatusChoices(models.TextChoices):
        CREATED = 'CREATED', 'Создан'
        DELIVERED = 'DELIVERED', 'Доставлен'
        PROCESSED = 'PROCESSED', 'В процессе'
        CANCELLED = 'CANCELLED', 'Отменён'
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    delivery_at = models.DateTimeField(
        verbose_name='Дата доставки',
        blank=True,
        null=True
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Пользователь'
    )
    address = models.CharField(
        max_length=256,
        verbose_name='Адрес'
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Корзина'
    )
    status = models.CharField(
        max_length=9,
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.CREATED,
        verbose_name='Статус публикации'
    )
    total_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Итого'
    )
