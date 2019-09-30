from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from django.db import models

from .models import Contacto

class CustomUserCreationForm(forms.Form):
    username   = forms.CharField(label='Usuario', min_length=4, max_length=25)
    email      = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Nombre', min_length=2, max_length=30)
    password1  = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2  = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Ya existe ese usuario.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Ya existe ese Email.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

class ContactCreationForm(forms.Form):
    user_id = forms.IntegerField(widget = forms.HiddenInput(), required=False)
    first_name = forms.CharField(label='Nombre', min_length=2, max_length=30)
    last_name  = forms.CharField(label='Apellido', min_length=2, max_length=30, required=False)
    phone = forms.CharField(label='Telefono', min_length=10, max_length=13, required=False)
    email = forms.CharField(label='Email', min_length=10, max_length=30, required=False)
    address = forms.CharField(label='Direccion', max_length=100, required=False)

    def save(self, commit=True):
        contact = Contacto(user_id=self.cleaned_data['user_id'],
                           first_name=self.cleaned_data['first_name'],
                           last_name=self.cleaned_data['last_name'],
                           phone=self.cleaned_data['phone'],
                           email=self.cleaned_data['email'],
                           address=self.cleaned_data['address'])
        contact.save()

        return True
