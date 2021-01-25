from django.db import models

from config import settings


class Review(models.Model):
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
        verbose_name='Дата создания'
    )
    published_at = models.DateField(
        verbose_name='Дата публикации'
    )
    status = models.CharField(
        max_length=20,
        verbose_name='Статус публикации'
    )

    def __str__(self):
        return self.author
