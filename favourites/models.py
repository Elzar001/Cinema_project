from django.db import models
from django.contrib.auth import get_user_model

from films.models import Film

User = get_user_model()


class Favourites(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='favourite')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourite')

    class Meta:
        verbose_name = 'Favourite'
        verbose_name_plural = 'Favourites'

    def __str__(self): return f'{self.film} added to favourites'
