from django.db import models
from django.contrib.auth.models import User, AbstractUser

PHONE_LABELS = (
    ('Celular','Celular'),
    ('Trabajo','Trabajo'),
    ('Casa', 'Casa'),
    ('Fijo', 'Fijo'),
    ('Otro', 'Otro')
)

EMAIL_LABELS = (
    ('Principal','Principal'),
    ('Casa','Casa'),
    ('Trabajo','Trabajo'),
    ('Otro', 'Otro')
)

ADDRESS_LABELS = (
    ('Casa', 'Casa'),
    ('Trabajo','Trabajo'),
    ('Otro', 'Otro')
)

GROUP_LABELS = (
    ('Todos', 'Todos'),
    ('Favoritos','Favoritos'),
    ('Amigos','Amigos'),
    ('Conocidos','Conocidos'),
    ('Trabajo','Trabajo'),
    ('Escuela','Escuela')
)

# Create your models here.
class Contact(models.Model): #AbstractUser
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    group = models.CharField(default="Todos", choices=GROUP_LABELS, max_length=20)
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f" {self.first_name} {self.last_name} ( {self.group} )"

class Phone(models.Model):
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    phone_label = models.CharField(default="Celular", choices=PHONE_LABELS, max_length=10)
    phone = models.CharField(max_length=13, blank=True)
    contact = models.ForeignKey(Contact, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.phone_label}: {self.phone}"

class Email(models.Model):
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    email_label = models.CharField(default="Principal", choices=EMAIL_LABELS, max_length=10)
    email = models.CharField(max_length=30, blank=True)
    contact = models.ForeignKey(Contact, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.email_label}: {self.email}"

class Address(models.Model):
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    address_label = models.CharField(default="Casa", choices=ADDRESS_LABELS, max_length=10)
    address = models.CharField(max_length=100, blank=True)
    contact = models.ForeignKey(Contact, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.address_label}: {self.address}"
