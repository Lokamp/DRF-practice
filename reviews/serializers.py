from rest_framework import serializers

from .models import Review
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'phone_number',
            'address'
        )


class ReviewSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True, required=False)

    class Meta:
        model = Review
        fields = (
            'id',
            'author',
            'status',
            'text',
            'created_at',
            'published_at',
        )
