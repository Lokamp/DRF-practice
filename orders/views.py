from rest_framework.viewsets import ModelViewSet

from orders.models import Order
from orders.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.order_by('id')
    serializer_class = OrderSerializer
