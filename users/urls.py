from django.urls import path
#from django.conf.urls import patterns, url

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("signup", views.signup_view, name="signup"),
    path("logout", views.logout_view, name="logout"),
    path("contact/<int:contact_id>/", views.contact_view, name="contact"),
    path("delete/<int:contact_id>/", views.delete_view, name="delete") #/<int:id>/
]
