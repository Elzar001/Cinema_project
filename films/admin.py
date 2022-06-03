from django.contrib import admin

from films.models import Film, Genre, Comment

admin.site.register(Genre)
admin.site.register(Film)
admin.site.register(Comment)
