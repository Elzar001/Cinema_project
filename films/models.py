from django.db import models

from account.serializers import User


class Genre(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, primary_key=True)

    def __str__(self): return self.name


class Film(models.Model):
    preview = models.ImageField(upload_to='images', blank=True, null=True)
    title = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='films')
    description = models.TextField()

    def __str__(self): return self.title


class Comment(models.Model):
    body = models.TextField()
    film = models.ForeignKey(Film, related_name='comment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)

    def __str__(self): return f'{self.owner} - {self.body}'
