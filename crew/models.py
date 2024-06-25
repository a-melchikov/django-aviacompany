from django.db import models


class CrewMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    flights = models.ManyToManyField("flights.Flight", related_name="crew_members")

    def __str__(self):
        return f"{self.name} ({self.role})"
