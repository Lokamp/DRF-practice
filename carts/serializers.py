from rest_framework.fields import ListField, SerializerMethodField, ReadOnlyField, CharField
from rest_framework.relations import PrimaryKeyRelatedField, StringRelatedField, SlugRelatedField
from rest_framework.serializers import ModelSerializer

from items.models import Item
from .models import Cart, CartItem


class ItemCartSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CartItemSerializer(ModelSerializer):
    item = ItemCartSerializer()

    class Meta:
        model = CartItem

        fields = [
            'id',
            'item',
            'quantity',
            'price',

        ]


class CartSerializer(ModelSerializer):
    items = CartItemSerializer(source='cartitem_set', many=True)

    class Meta:
        model = Cart
        fields = ['id', 'items']
