from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from django.db import models
from django.forms import ModelForm

from .models import Contact, Phone, Email, Address

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
            self.cleaned_data['first_name'],
            self.cleaned_data['password1']
        )
        return user

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['group', 'first_name', 'last_name']
        labels = {
                   'group': 'Grupo',
                   'first_name': 'Nombre',
                   'last_name': 'Apellido'
        }
        exclude = ['user']

class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = ['user', 'contact', 'phone_label', 'phone']
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': 'Agregar Teléfono'})
        }
        exclude = ['user', 'contact']

class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['email_label', 'email']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Agregar Email'})
        }
        exclude = ['user', 'contact']

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['address_label', 'address']
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Agregar Dirección'})
        }
        exclude = ['user', 'contact']
