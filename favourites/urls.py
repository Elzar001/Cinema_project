from django.urls import path
from . import views

urlpatterns = [
    path('favourites/', views.FavouritesView.as_view()),
    path('favourites/add/', views.AddToFavouritesView.as_view()),
]
