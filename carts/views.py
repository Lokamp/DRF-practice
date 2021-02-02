from rest_framework import mixins
from rest_framework.generics import RetrieveAPIView, ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from carts.models import Cart, CartItem
from carts.serializers import CartSerializer, CartItemSerializer
from items.models import Item
from users.models import User


class CartViewSet(mixins.ListModelMixin,
                  GenericViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Cart.objects.filter(user_id=self.request.user)
        return queryset


class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = get_object_or_404(Cart, user=self.request.user)
        # user = Cart.objects.get(user_id=self.request.user)
        # queryset = CartItem.objects.filter(cart_id=user)
        print(queryset)
        return queryset.cart.all()

    def get_object(self):
        cart = get_object_or_404(Cart, user=self.request.user)
        id = self.kwargs['pk']
        cartitem = get_object_or_404(cart.cart, pk=id)
        return cartitem