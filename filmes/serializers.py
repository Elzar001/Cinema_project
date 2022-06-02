from rest_framework import serializers

from filmes.models import Genre, Film


class GenreSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Genre
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
