from django.test import TestCase
from ..models import Departament, Employee
from ..serializers import EmployeeSerializer


class EmployeeSerializerTest(TestCase):
    """ Test employee serializer """

    def setUp(self):
        dpt_arch = Departament.objects.create(name='Architecture')
        self.data = {'name': 'John Lennon', 'email': 'lennon@beatles.net', 'departament' : dpt_arch}

    def test_employee_serializer(self):
        serializer = EmployeeSerializer(self.data)
        self.assertCountEqual(serializer.data.keys(), ['name', 'email', 'departament'])

