from django.test import TestCase
from ..models import Departament, Employee


class DepartamentTest(TestCase):
    """ Test module for Departament model """

    def setUp(self):
        Departament.objects.create(name='Architecture')
        Departament.objects.create(name='E-commerce')

    def test_objects_get(self):
        dpt_arch = Departament.objects.get(name='Architecture')
        dpt_comm = Departament.objects.get(name='E-commerce')
        self.assertEqual(dpt_arch.name, 'Architecture')
        self.assertEqual(dpt_comm.name, 'E-commerce')

    def test_objects_update(self):
        dpt = Departament.objects.get(name='Architecture')
        dpt.name = 'Musician'
        dpt.save()
        self.assertEqual(dpt.name, 'Musician')


class EmployeeTest(TestCase):
    """ Test module for Employee model """

    def setUp(self):
        dpt_arch = Departament.objects.create(name='Architecture')
        dpt_comm = Departament.objects.create(name='E-commerce')
        Employee.objects.create(
            name='John Lennon', email='lennon@beatles.net', departament=dpt_arch)
        Employee.objects.create(
            name='Ringo Starr', email='starr@beatles.net', departament=dpt_comm)

    def test_objects_get(self):
        john = Employee.objects.get(name='John Lennon')
        ringo = Employee.objects.get(name='Ringo Starr')
        self.assertEqual(john.email, 'lennon@beatles.net')
        self.assertEqual(ringo.name, 'Ringo Starr')
        self.assertEqual(john.departament.name, 'Architecture')

    def test_objects_update(self):
        john = Employee.objects.get(name='John Lennon')
        john.email = 'lennon@beatles.com'
        john.departament.name = 'Musician'
        john.save()

        self.assertEqual(john.email, 'lennon@beatles.com')
        self.assertEqual(john.departament.name, 'Musician')
