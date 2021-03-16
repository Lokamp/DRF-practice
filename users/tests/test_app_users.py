from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserRegViewSetTestCase(APITestCase):

    def test_create_account(self):
        url = reverse('users:register')
        data = {
            'username': 'Alex',
            'password': '1234567807',
            'email': 'test14@email.com',
            'first_name': 'Александр',
            'last_name': 'Петров',
            'middle_name': 'Васильевич',
            'phone_number': '9260000000',
            'address': 'net Street'
        }
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'Alex')


class UserCurrentViewSetTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='Alex4',
            password='1234567807',
            email='test14@emailcom',
            first_name='Александр',
            last_name='Петров',
            middle_name='Васильевич',
            phone_number='9260000000',
            address='net Street'
        )
        self.url = reverse('users:current')

    def test_unauthorized(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, {'detail': 'Authentication credentials were not provided.'})

    def test_current_user(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                'id': self.user.id,
                'first_name': self.user.first_name,
                'last_name': self.user.last_name,
                'email': self.user.email,
                'middle_name': self.user.middle_name,
                'phone_number': self.user.phone_number,
                'address': self.user.address
            }
        )
