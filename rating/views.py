from rest_framework import generics, permissions

from . import serializers


class RatingCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.RatingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
