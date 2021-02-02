from rest_framework.serializers import ModelSerializer

from items.models import Item
from .models import Cart, CartItem


class ItemSerializer(ModelSerializer):
    class Meta:

        model = Item
        fields = [
            'id',
            'title',
            'description',
            'image',
            'weight',
            'price'
        ]


class CartItemSerializer(ModelSerializer):
    item = ItemSerializer(required=False)

    class Meta:
        model = CartItem
        fields = [
            'id',
            'item',
            'item_id',
            'quantity',
            'price',
        ]

        extra_kwargs = {'price': {'required': False}}

        # def create(self):
        #     Cart.objects.get_or_create()
        #     CurrentUserDefault()

class CartSerializer(ModelSerializer):
    items = CartItemSerializer(source='cart', many=True)

    class Meta:
        model = Cart
        fields = ['id', 'items']
