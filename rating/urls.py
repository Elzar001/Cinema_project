from . import views
from django.urls import path

urlpatterns =[
    path('rating/create/', views.RatingCreateApiView.as_view()),
]
