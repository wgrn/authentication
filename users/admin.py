from django.contrib import admin

from .models import Contacto, Phone, Email, Address

# Register your models here.
admin.site.register(Contacto)
admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(Address)
