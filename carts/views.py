from rest_framework.generics import RetrieveAPIView, ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from carts.models import Cart
from carts.serializers import CartSerializer


class CartViewSet(ListAPIView):
    # queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     queryset = get_object_or_404(Cart, user_id=self.request.user)
    #     return queryset

    def get_queryset(self):
        return Cart.objects.filter(user_id=self.request.user)

