from django.contrib import admin
from .models import Flight


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = [
        "flight_number",
        "departure_location",
        "arrival_location",
        "formatted_departure_time",
        "formatted_arrival_time",
    ]
    filter_horizontal = ["crew"]

    def formatted_departure_time(self, obj):
        return obj.departure_time.strftime("%d.%m.%Y %H:%M")

    formatted_departure_time.short_description = "Время отправления"

    def formatted_arrival_time(self, obj):
        return obj.arrival_time.strftime("%d.%m.%Y %H:%M")

    formatted_arrival_time.short_description = "Время прибытия"

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "flight_number",
                    ("departure_location", "arrival_location"),
                    ("departure_time", "arrival_time"),
                    "crew",
                )
            },
        ),
    )

    verbose_name = "Рейс"
    verbose_name_plural = "Рейсы"
