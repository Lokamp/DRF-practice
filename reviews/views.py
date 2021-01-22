from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from reviews.models import Review


@api_view(http_method_names=['GET'])
def get_review_view(request, pk):
    review = get_object_or_404(Review, id=pk)
    return Response({
        'id': review.id,
    })
