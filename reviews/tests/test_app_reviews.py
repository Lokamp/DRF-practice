from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class ReviewViewSetTestCase(APITestCase):
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
        self.url = reverse('reviews-list')

    def test_crate_review(self):
        data = {
            'text': 'Какой славный товар'
        }
        self.client.force_authenticate(self.user)
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_review(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
