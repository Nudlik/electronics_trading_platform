from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse


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
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
