from django.contrib import admin
from .models import Flight


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = [
        "flight_number",
        "departure_location",
        "arrival_location",
        "departure_time",
        "arrival_time",
    ]
    filter_horizontal = ["crew"]
