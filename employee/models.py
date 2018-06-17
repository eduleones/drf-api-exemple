from django.db import models


class Departament(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    departament = models.ForeignKey(Departament,
                                    models.SET_NULL,
                                    blank=True,
                                    null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
