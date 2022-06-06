from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from . import serializers

from films.models import Film, Genre, Comment
from .permissions import IsAuthor
from .serializers import CommentSerializer


class StandardPaginationClass(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 1000


class FilmViewSet(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = serializers.FilmSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('genre', )
    search_fields = ('title',)
    pagination_class = StandardPaginationClass

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy',):
            return (permissions.IsAdminUser(), )
        else:
            return (permissions.AllowAny(), )


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    permission_classes = (permissions.IsAdminUser,)


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthor]


# class CommentViewSet(ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = (permissions.AllowAny(),)
#
#     def get_permissions(self):
#         if self.action in ('create', 'update', 'partial_update', 'destroy',):
#             return [IsAuthor()]
#         else:
#             return (permissions.AllowAny(),)


def index(request):
    film = Film.objects.all()
    return render(request, 'index.html', {'film': film})
