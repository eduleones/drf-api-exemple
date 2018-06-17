import json
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from ..models import Departament, Employee
from ..serializers import EmployeeSerializer


class CreateEmployeeTest(APITestCase):
    def setUp(self):

        self.url = reverse('employee-list')
        self.client = APIClient()

        self.valid_data = {
            'name': 'John Lennon',
            'email': 'lennon@beatles.net',
            'departament': 'Musician'
        }
        self.invalid_data = {
            'name': 'Ringo Starr',
            'email': 'ringo.com',
            'departament': ''
        }

    def test_create_valid_data(self):
        response = self.client.post(self.url, data=json.dumps(
            self.valid_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_data(self):
        response = self.client.post(self.url, data=json.dumps(
            self.invalid_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateEmployeeTest(APITestCase):
    def setUp(self):

        self.client = APIClient()

        dpt_arch = Departament.objects.create(name='Architecture')
        dpt_comm = Departament.objects.create(name='E-commerce')
        self.john = Employee.objects.create(
            name='John Lennon', email='lennon@beatles.net', departament=dpt_arch)
        self.ringo = Employee.objects.create(
            name='Ringo Starr', email='starr@beatles.net', departament=dpt_comm)

        self.valid_data = {
            'name': 'John Lennon',
            'email': 'lennon@beatles.com',
            'departament': 'Musician'
        }
        self.invalid_data = {
            'name': 'Ringo Starr',
            'email': 'ringo.com',
            'departament': ''
        }

    def test_valid_update_data(self):

        url = reverse('employee-detail', kwargs={'pk': self.john.pk})
        response = self.client.put(url, data=json.dumps(
            self.valid_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_data(self):
        url = reverse('employee-detail', kwargs={'pk': self.ringo.pk})
        response = self.client.put(url, data=json.dumps(
            self.invalid_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteEmployeeTest(APITestCase):
    def setUp(self):

        self.client = APIClient()

        dpt_arch = Departament.objects.create(name='Architecture')
        self.john = Employee.objects.create(
            name='John Lennon', email='lennon@beatles.net', departament=dpt_arch)

    def test_valid_delete_data(self):
        url = reverse('employee-detail', kwargs={'pk': self.john.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_data(self):
        url = reverse('employee-detail', kwargs={'pk': 8787832})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
