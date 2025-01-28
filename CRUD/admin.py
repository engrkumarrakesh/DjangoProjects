from django.contrib import admin
from CRUD.models import *


# Register your models here.

# admin.site.register(Employee)
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.get_fields()]

# admin.site.register(Employee, EmployeeAdmin)
