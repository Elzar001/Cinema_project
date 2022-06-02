from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from . import serializers

from filmes.models import Film, Genre


class StandardPaginationClass(PageNumberPagination):
    page_size = 1
    page_query_param = 'page_size'
    max_page_size = 1000


class FilmViewSet(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = serializers.FilmSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('genre', )
    search_fields = ('title',)
    pagination_class = StandardPaginationClass

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy',):
            return [permissions.IsAdminUser()]
        else:
            return [permissions.AllowAny()]


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    permission_classes = [permissions.IsAdminUser, ]
