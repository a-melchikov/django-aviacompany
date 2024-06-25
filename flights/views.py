from django.shortcuts import render, get_object_or_404
from .models import Flight


def flight_list(request):
    flights = Flight.objects.all()
    return render(request, "flight_list.html", {"flights": flights})


def flight_detail(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    return render(request, "flight_detail.html", {"flight": flight})
