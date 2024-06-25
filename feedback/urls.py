from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact, name="contacts"),
    path("contacts_success/", views.contacts_success, name="contacts_success"),
]
