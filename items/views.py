from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from items.models import Item
from items.serializers import ItemSerializer


class ItemViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'price': ['exact', 'gt', 'gte', 'lt', 'lte'],
        'weight': ['exact', 'gt', 'gte', 'lt', 'lte']
    }
    ordering = ['id']
