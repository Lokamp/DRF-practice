from django.db import models

from users.models import User


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="review"
    )
    text = models.TextField()
    created_at = models.DateField()
    published_at = models.DateField()
    status = models.CharField(
        max_length=20
    )
