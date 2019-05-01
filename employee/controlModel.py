from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=15)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name