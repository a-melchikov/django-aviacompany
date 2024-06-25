from django.shortcuts import render, get_object_or_404
from flights.models import Flight


def crew_list(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    crew_members = flight.crew.all()
    return render(
        request, "crew_list.html", {"flight": flight, "crew_members": crew_members}
    )
