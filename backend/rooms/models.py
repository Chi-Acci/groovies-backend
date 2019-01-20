from django.db import models

from . import constants
from .managers import RoomManager


class Room(models.Model):
    objects = RoomManager()

    slug = models.SlugField(
        max_length=20,
        unique=True,
        null=False,
        default=None
    )

    mood = models.CharField(
        choices=[(option['key'], option['key']) for option in constants.moods()],
        max_length=max([len(option['key']) for option in constants.moods()]),
        default=constants.MOOD_ANY['key'],
        null=False,
    )

    admin = models.ForeignKey(to='users.User',
                              related_name='rooms_as_admin',
                              null=False,
                              on_delete=models.deletion.CASCADE)

    users = models.ManyToManyField(to='users.User', related_name='rooms')

    def initialize_users(self) -> None:
        self.users.add(self.admin)
        self.save()