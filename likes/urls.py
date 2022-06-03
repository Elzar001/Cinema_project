from django.urls import path
from . import views

urlpatterns = [
    path('likes/', views.LikesView.as_view()),
    path('likes/add-like/', views.LikesCreateView.as_view())
]