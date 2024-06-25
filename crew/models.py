from django.db import models


class CrewMember(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    role = models.CharField(max_length=50, verbose_name="Роль")
    flights = models.ManyToManyField(
        "flights.Flight", related_name="crew_members", verbose_name="Рейсы"
    )

    class Meta:
        verbose_name = "Член экипажа"
        verbose_name_plural = "Члены экипажа"

    def __str__(self):
        return f"{self.name} ({self.role})"
