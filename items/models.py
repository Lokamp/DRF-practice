from django.db import models


class Item(models.Model):
    title = models.CharField(
        max_length=220
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to='image'
    )
    weight = models.IntegerField()
    price = models.DecimalField(
        max_digits=100, decimal_places=4
    )
