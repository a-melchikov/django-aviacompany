from django.urls import path
from . import views

urlpatterns = [
    path("<int:flight_id>/", views.crew_list, name="crew_list"),
]
