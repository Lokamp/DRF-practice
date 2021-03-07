from django.http import Http404
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from carts.models import Cart, CartItem
from carts.serializers import CartSerializer, CartItemSerializer
from items.models import Item


class CartViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return super().get_queryset().filter(user=self.request.user)

    # def perform_create(self, serializer):
    #     cart = super().get_queryset().filter(user=self.request.user)
    #     print(cart)
    #     items = cart.cart_items.all()
    #     total_cost = sum([price.total_price for price in items])
    #     serializer.save(total_cost=total_cost)


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_cart(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

    @staticmethod
    def get_item(pk):
        return Item.objects.get(pk=pk)

    def get_queryset(self):
        return super().get_queryset().filter(cart=self.get_cart())

    def perform_create(self, serializer):
        # print(serializer)
        # print('_____________')
        # print(serializer.__dict__)
        # print('_____________')
        # print(self.request.data)
        if CartItem.objects.filter(
            cart=self.get_cart(),
            item=self.get_item(self.request.data['item'])
        ).exists():
            raise Http404
        serializer.save(
            cart=self.get_cart(),
            price=self.get_item(self.request.data['item']).price
        )
