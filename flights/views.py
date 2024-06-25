from datetime import datetime
from django.shortcuts import render, get_object_or_404
from .models import Flight


def flight_list(request):
    flights = Flight.objects.all()
    return render(request, "flight_list.html", {"flights": flights})


def flight_detail(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    return render(request, "flight_detail.html", {"flight": flight})


def search_flights(request):
    start_date = request.GET.get("start_date")
    departure_location = request.GET.get("departure_location")
    arrival_location = request.GET.get("arrival_location")

    flights = Flight.objects.all()

    if start_date:
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        flights = flights.filter(departure_time__date=start_date)

    if departure_location:
        flights = flights.filter(departure_location__icontains=departure_location)

    if arrival_location:
        flights = flights.filter(arrival_location__icontains=arrival_location)

    context = {
        "flights": flights,
    }

    return render(request, "flight_list.html", context)
