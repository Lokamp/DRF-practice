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

        ref_name = None


class CartItemSerializer(ModelSerializer):
    item_object = ItemSerializer(required=False, read_only=True, source='item')

    class Meta:
        model = CartItem
        fields = [
            'id',
            'item_object',
            'item',
            'quantity',
            'price',
            'total_price',
        ]

        read_only_fields = [
            'price',
        ]

        ref_name = None


class CartSerializer(ModelSerializer):
    items = CartItemSerializer(source='cart_items', many=True)
    # total_cost = SerializerMethodField(read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_cost']

        ref_name = None
