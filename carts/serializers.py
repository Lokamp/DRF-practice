from rest_framework.fields import EmailField, ReadOnlyField, ModelField
from rest_framework.serializers import ModelSerializer

from items.models import Item
from users.models import User
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
    item_object = ItemSerializer(required=False, read_only=True, source='item')
    email = ModelField(model_field=User.email)

    class Meta:
        model = CartItem
        fields = [
            'id',
            'item_object',
            'item',
            'quantity',
            'price',
            'total_price',
            'email'
        ]

        read_only_fields = [
            'price',
        ]


class CartSerializer(ModelSerializer):
    items = CartItemSerializer(source='cart_items', many=True)

    class Meta:
        model = Cart
        fields = ['id', 'items']
