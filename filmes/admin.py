from django.contrib import admin

from filmes.models import Film, Genre

admin.site.register(Genre)
admin.site.register(Film)