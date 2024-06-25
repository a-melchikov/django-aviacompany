from django.db import models
from crew.models import CrewMember


class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    departure_location = models.CharField(max_length=100)
    arrival_location = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    crew = models.ManyToManyField(CrewMember, related_name="assigned_flights")

    def __str__(self):
        return f"{self.flight_number} from {self.departure_location} to {self.arrival_location}"
