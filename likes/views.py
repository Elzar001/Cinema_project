from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import LikesSerializer
from .models import Likes


class LikesView(generics.ListAPIView):
    serializer_class = LikesSerializer
    queryset = Likes.objects.all()


class LikesCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
