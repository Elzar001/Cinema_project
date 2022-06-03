from django.db import models
from django.contrib.auth import get_user_model

from films.models import Film

User = get_user_model()


class Likes(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self): return f'{self.film} liked'
