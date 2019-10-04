from django.contrib import admin

from .models import Contact, Phone, Email, Address

# Register your models here.
admin.site.register(Contact)
admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(Address)
