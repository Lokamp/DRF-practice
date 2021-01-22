from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from users.models import User


@api_view(http_method_names=['GET'])
def get_user_view(request, pk):
    user = get_object_or_404(User, id=pk)
    return Response({
        'id': user.id,
    })
