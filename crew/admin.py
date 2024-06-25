from django.contrib import admin
from .models import CrewMember


@admin.register(CrewMember)
class CrewMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "display_flights")
    search_fields = ("name", "role")
    filter_horizontal = ("flights",)

    def display_flights(self, obj):
        return ", ".join([flight.flight_number for flight in obj.flights.all()])

    display_flights.short_description = "Рейсы"
