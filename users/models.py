from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Phone(models.Model):
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.phone}"

class Email(models.Model):
    email = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.email}"

class Address(models.Model):
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.address}"

class Contacto(models.Model):
    user_id = models.IntegerField()
    group = models.CharField(default="Todos" ,max_length=20)
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

"""
class Contacto(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario")
    contactos = models.ManyToManyField(Persona, blank=True, related_name="contactos")

    def __str__(self):
        return f"{self.contactos.first_name} {self.contactos.last_name}"
"""
