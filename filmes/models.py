from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, primary_key=True)

    def __str__(self): return self.name


class Film(models.Model):
    preview = models.ImageField(upload_to='images', blank=True, null=True)
    title = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='filmes')
    description = models.TextField()

    def __str__(self): return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Film'
        verbose_name_plural = 'Filmes'
