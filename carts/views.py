from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from carts.models import Cart
from carts.serializers import CartSerializer


class CartViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    pagination_class = PageNumberPagination
