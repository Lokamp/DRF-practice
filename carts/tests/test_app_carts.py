from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from carts.models import Cart
from users.models import User


class CartViewSetTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='Alex1',
            password='12345678',
            email='test@gmail.com',
            first_name='alex',
            last_name='alex1',
            middle_name='ooo',
            phone_number='9260000000',
            address='net Street'
        )
        self.cart = Cart.objects.create(user=self.user)
        self.url = reverse('carts-list')

    def test_unauthorized(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, {'detail': 'Authentication credentials were not provided.'})

    def test_get_cart(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
