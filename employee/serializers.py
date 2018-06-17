from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from .models import Departament, Employee


class EmployeeSerializer(serializers.ModelSerializer):

    departament = serializers.SlugRelatedField(
        slug_field='name', queryset=Departament.objects.all())

    class Meta:
        model = Employee
        fields = ('name', 'email', 'departament',)

