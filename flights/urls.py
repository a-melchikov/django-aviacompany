from django.urls import path
from . import views

urlpatterns = [
    path("", views.flight_list, name="flight_list"),
    path("<int:flight_id>/", views.flight_detail, name="flight_detail"),
]
