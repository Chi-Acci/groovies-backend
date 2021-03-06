from django.db import models

from .managers import RatingsManager


class Rating(models.Model):
    objects = RatingsManager()

    user = models.ForeignKey(
        to='users.User',
        related_name='ratings',
        null=False,
        on_delete=models.deletion.CASCADE
    )

    movie = models.ForeignKey(
        to='movies.Movie',
        related_name='ratings',
        null=False,
        on_delete=models.deletion.CASCADE
    )

    score = models.IntegerField(
        null=True,
        default=None
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ['user', 'movie']
