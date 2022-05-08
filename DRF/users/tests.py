import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate,
APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import AuthorViewSet
from .models import CustomUser


class TestUserViewSet(TestCase):
	def test_get_list(self):
		factory = APIRequestFactory()
		request = factory.get('/api/users/')
		view = UserViewSet.as_view({'get': 'list'})
		response = view(request)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		
	def test_get_detail(self):
		user = User.objects.create(email='Boris', date_joined=17.03.2020)
		client = APIClient()
		response = client.get(f'/api/users/{users.id}/')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		
