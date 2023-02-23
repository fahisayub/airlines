from django.shortcuts import render,reverse

# Create your views here.
from .models import Flight, Airport, Passenger
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "flights/index.html", {"flights": Flight.objects.all()})


def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flight=flight).all()
    return render(
        request,
        "flights/flight.html",
        {"flight": flight, "passengers": passengers, "non_passengers": non_passengers},
    )


def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)  # pk= primary key =id
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(id=passenger_id)
        passenger.flight.add(flight)

        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
