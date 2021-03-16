from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Review.objects.order_by('id')
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
