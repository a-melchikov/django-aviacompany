from django.db import models
from crew.models import CrewMember


class Flight(models.Model):
    flight_number = models.CharField(max_length=10, verbose_name="Номер рейса")
    departure_location = models.CharField(
        max_length=100, verbose_name="Место отправления"
    )
    arrival_location = models.CharField(max_length=100, verbose_name="Место прибытия")
    departure_time = models.DateTimeField(verbose_name="Время отправления")
    arrival_time = models.DateTimeField(verbose_name="Время прибытия")
    crew = models.ManyToManyField(
        CrewMember, related_name="assigned_flights", verbose_name="Экипаж"
    )

    class Meta:
        verbose_name = "Рейс"
        verbose_name_plural = "Рейсы"

    def __str__(self):
        return f"{self.flight_number} from {self.departure_location} to {self.arrival_location}"
