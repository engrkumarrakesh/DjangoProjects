from django.contrib import admin
from function_based_view_01.models import Student
from url_patterns_02.models import Student
@admin.register(home)
class StudentAdmin(admin.ModelAdmin):
# list_display = ('name', 'roll', 'city')
# Register your models here.