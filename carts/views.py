from django.http import Http404
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from carts.models import Cart, CartItem
from carts.serializers import CartSerializer, CartItemSerializer


class CartViewSet(mixins.ListModelMixin,
                  GenericViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Cart.objects.filter(user=self.request.user)
        return queryset


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_cart(self):
        cart = Cart.objects.filter(user=self.request.user).latest('id')
        if not cart:
            Cart.objects.create(user=self.request.user)
        return cart

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['cart'] = self.get_cart()
        return context

    def get_queryset(self):
        return super().get_queryset().filter(cart=self.get_cart())

    def perform_create(self, serializer):
        cart_item = CartItem(**serializer.validated_data)
        print(CartItem.objects.filter(cart=self.get_cart(), item=cart_item.item).exists())
        if CartItem.objects.filter(cart=self.get_cart(), item=cart_item.item).exists():
            raise Http404
        cart_item.cart = self.get_cart()
        cart_item.price = cart_item.item.price
        cart_item.save()
