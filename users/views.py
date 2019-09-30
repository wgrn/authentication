from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, ContactCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Contacto

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    if request.method == 'POST':
        post_values = request.POST.copy()
        post_values['user_id'] = request.user.id
        contact = ContactCreationForm(post_values)
        #        <!--{{ value|default_if_none=str(user.id) }}-->
        if contact.is_valid():
            contact.save()
            messages.success(request, '') # Contact successfully created
            return HttpResponseRedirect(reverse("index"))
    else:
        contact = ContactCreationForm()
    context = {
        "user": request.user,
        "contactos": Contacto.objects.filter(user_id=request.user.id),
        "form": contact
    }

    return render(request, "users/user.html", context)

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

def add_contact(request, user_id):
    try:
        pass
    except Exception as e:
        raise

"""
def add_contact(request, user_id):
    try:
        contact_id = int(request.POST["contact"])
        flight = Flight.objects.get(pk=flight_id)
        contact = Contacto.objects.get(pk=contact_id)
    except KeyError:
        return render(request, "flights/error.html", {"message": "No selection."})
    except Flight.DoesNotExist:
        return render(request, "flights/error.html", {"message": "No flight."})
    except Passenger.DoesNotExist:
        return render(request, "flights/error.html", {"message": "No passenger."})
    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
"""
