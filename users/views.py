from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, ContactForm, PhoneForm, EmailForm, AddressForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Contact, Phone, Email, Address

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    if request.method == 'POST':
        contact = ContactForm(request.POST)

        if contact.is_valid():
            contact.instance.user = request.user #User.objects.get(pk=request.user.pk)
            c = contact.save()
            messages.success(request, '') # Contact successfully created

            phone = PhoneForm(request.POST)
            if phone.is_valid() and phone.instance.phone != '':
                phone.instance.user = request.user
                phone.instance.contact = c #Contact.objects.get(id=c.id)
                phone.save()

            else:
                print("############################ Phone", phone.errors)

            email = EmailForm(request.POST)
            if email.is_valid() and email.instance.email != '': # and email.instance.email != '':
                email.instance.user = request.user
                email.instance.contact = c
                email.save()
            else:
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Email", email.errors)

            address = AddressForm(request.POST)
            if address.is_valid() and address.instance.address != '': #and address.instance.address != '':
                address.instance.user = request.user
                address.instance.contact = c
                address.save()
            else:
                print("&&&&&&&&&&&&&&&&&&&&&&&&&&&& Address", address.errors)

            return HttpResponseRedirect(reverse("index"))
    else:
        contact = ContactForm()
        phone = PhoneForm()
        email = EmailForm()
        address = AddressForm()

    context = {
        "user": request.user,
        "contacts": Contact.objects.filter(user=request.user.id),
        "phones": Phone.objects.filter(user=request.user.id),
        "emails": Email.objects.filter(user=request.user.id),
        "addresses": Address.objects.filter(user=request.user.id),
        "form": contact,
        "form2": phone,
        "form3": email,
        "form4": address
    }

    return render(request, "users/user.html", context)

def contact_view(request, contact_id):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})

    contact = Contact.objects.get(id=contact_id)
    contact_form = ContactForm(request.POST or None, instance=contact)

    phone = PhoneForm(request.POST or None)
    email = EmailForm(request.POST or None)
    address = AddressForm(request.POST or None)

    if contact_form.is_valid():
        contact_form.save()

        if phone.is_valid() and phone.instance.phone != '':
            phone.instance.user = request.user
            phone.instance.contact = contact #Contact.objects.get(id=c.id)
            phone.save()
        else:
            print("############################ Phone", phone.errors)

        if email.is_valid() and email.instance.email != '': # and email.instance.email != '':
            email.instance.user = request.user
            email.instance.contact = contact
            email.save()
        else:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Email", email.errors)

        if address.is_valid() and address.instance.address != '': #and address.instance.address != '':
            address.instance.user = request.user
            address.instance.contact = contact
            address.save()
        else:
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&& Address", address.errors)

        return HttpResponseRedirect(reverse("contact", kwargs={"contact_id": contact_id}))

    context = {
        #"user": request.user,
        "contact": contact, #Contact.objects.get(id=contact_id),
        "phones": Phone.objects.filter(user=request.user.id, contact=contact),
        "emails": Email.objects.filter(user=request.user.id, contact=contact),
        "addresses": Address.objects.filter(user=request.user.id, contact=contact),
        "form": contact_form,
        "form2": phone,
        "form3": email,
        "form4": address
    }

    return render(request, "users/contact.html", context)

def delete_view(request, contact_id):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})

    contact = Contact.objects.get(id=contact_id)

    if request.method == 'POST':
        contact.delete()
        return HttpResponseRedirect(reverse("index"))

    return render(request, "users/delete.html", {'contact': contact})

def signup_view(request):
    if request.method == 'POST':
        #f = UserCreationForm(request.POST)
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, '') # Account created successfully
            return HttpResponseRedirect(reverse("index"))
    else:
        #f = UserCreationForm()
        f = CustomUserCreationForm()

    return render(request, "users/signup.html", {"form": f})

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "users/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})
