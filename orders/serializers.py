from rest_framework.serializers import ModelSerializer

from items.models import Item
from orders.models import Order


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'id',
            'title',
            'description',
            'image',
            'weight',
            'price'
            )

        ref_name = None


class OrderSerializer(ModelSerializer):
    item = ItemSerializer(read_only=True, required=False)

    class Meta:
        model = Order
        fields = ('id',
                  'item',
                  'created_at',
                  'delivery_at',
                  'recipient',
                  'address',
                  'cart',
                  'status',
                  'total_cost',
                  )
