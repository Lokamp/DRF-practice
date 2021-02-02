from rest_framework.fields import CharField, EmailField, HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from .models import User


class UserRegSerializer(ModelSerializer):
    username = CharField(
        max_length=100,
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all(), message='Имя уже занято'),
        ],
    )
    email = EmailField(
        max_length=255,
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all(), message='Email уже занят'),
        ],
    )

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'phone_number',
            'address'
        ]

        # extra_kwargs = {'id': {'read_only': True}}


class UserCurrentSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'middle_name',
            'phone_number',
            'address'
        ]
