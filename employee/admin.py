from django.contrib import admin
from .models import Departament, Employee


class DepartamentAdmin(admin.ModelAdmin):

    list_display = ['name']
    search_fields = ['name']


admin.site.register(Departament, DepartamentAdmin)


class EmployeeAdmin(admin.ModelAdmin):

    list_display = ['pk', 'name', 'email', 'departament']
    search_fields = ['pk', 'name', 'email', 'departament__name']


admin.site.register(Employee, EmployeeAdmin)
