from django.db import models


class Item(models.Model):
    title = models.CharField(
        max_length=220,
        verbose_name='Заголовок'
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to='image',
        verbose_name='Изображение'
    )
    weight = models.IntegerField(
        verbose_name='Вес'
    )  # Вес в граммах
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена'
    )

    def __str__(self):
        return self.title
