from django.db import models

# Create your models here.
class Employee (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name