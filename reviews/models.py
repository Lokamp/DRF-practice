from django.db import models

from config import settings


class Review(models.Model):
    class ReviewStatusChoices(models.TextChoices):
        MODERATION = 'MOD', 'На модерации'
        PUBLISHED = 'PUB', 'Опубликован'
        REJECTED = 'REJ', 'Отклонен'

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name='Автор'
    )
    text = models.TextField(
        verbose_name='Отзыв'
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    published_at = models.DateField(
        verbose_name='Дата публикации',
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=3,
        choices=ReviewStatusChoices.choices,
        default=ReviewStatusChoices.MODERATION,
        verbose_name='Статус публикации'
    )

    def __str__(self):
        return f'{self.author}'
