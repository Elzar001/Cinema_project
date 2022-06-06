from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('films', views.FilmViewSet),
router.register('genres', views.GenreViewSet),

urlpatterns = [
    path('', include(router.urls)),
    path('comments/', views.CommentListCreateView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
    path('', views.index),
]
