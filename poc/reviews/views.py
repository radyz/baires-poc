from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from reviews.models import Review
from reviews.serializers import ReviewModelSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the details of a review as long as the requesting user is the
    creator, otherwise a NotFound status code will be returned

    list:
    Return a list of all the existing reviews for which the requesting user
    has access to.

    create:
    Create a new review instance.

    The ip address value gets automatically
    extracted from the request object, if it doesn't exist then a BadRequest
    error is raised.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewModelSerializer
    ordering = ('id',)

    def get_queryset(self):
        return Review.objects \
            .filter(reviewer=self.request.user) \
            .select_related('company')

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)
