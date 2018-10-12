from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from reviews.models import Review
from reviews.serializers import ReviewModelSerializer


class ReviewViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer
    ordering = ('id',)

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)
