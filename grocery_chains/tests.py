from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse

from grocery_chains.models import GroceryChain


class PermissionTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username='test', password='test')

    def test_permission_good(self):
        url = reverse('grocery_chains:chains-list')
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_permission_bad(self):
        url = reverse('grocery_chains:chains-list')
        self.user.is_active = False
        self.user.save()
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class GroceryChainsTestCase(TestCase):

    def setUp(self):
        self.user1 = get_user_model().objects.create(username='test', password='test')

        self.chain1 = GroceryChain.objects.create(
            name='chain1',
            type_structure='factory',
            provider=None,
            owner=self.user1,
            email='1@1.ru',
            country='Russia',
            city='Moscow',
            street='Lenina',
            house_number='1'
        )

    def test_grocery_chains(self):
        data = {
            'debt': 100
        }
        url = reverse('grocery_chains:chains-detail', args=[self.chain1.id])
        self.client.force_login(self.user1)
        response = self.client.patch(url, data, 'application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.chain1.debt, 0)
