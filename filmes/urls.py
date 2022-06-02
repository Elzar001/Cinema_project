from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('filmes', views.FilmViewSet)
router.register('genres', views.GenreViewSet)

urlpatterns = [
    path('', include(router.urls))
]
