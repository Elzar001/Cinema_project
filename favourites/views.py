from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Favourites
from .serializers import FavouritesSerializer


class FavouritesView(generics.ListAPIView):
    serializer_class = FavouritesSerializer
    queryset = Favourites.objects.all()
    permission_classes = [IsAuthenticated]


class AddToFavouritesView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Favourites.objects.all()
    serializer_class = FavouritesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
