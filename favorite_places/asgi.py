from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Place
import random

def get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def index(request):
    session_key = get_session_key(request)
    places = Place.objects.filter(session_key=session_key)
    chosen_place = None
    if request.method == "POST" and places.exists():
        weights = [p.rating for p in places]
        chosen_place = random.choices(list(places), weights=weights, k=1)[0]
    return render(request, "places_to_go/index.html", {"chosen_place": chosen_place})

def places_list(request):
    session_key = get_session_key(request)
    places = Place.objects.filter(session_key=session_key)
    return render(request, "places_to_go/places_list.html", {"places": places})

def place_detail(request, pk):
    session_key = get_session_key(request)
    place = get_object_or_404(Place, pk=pk, session_key=session_key)
    return render(request, "places_to_go/place_detail.html", {"place": place})

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ["title", "description", "place_type", "location", "rating"]

def add_place(request):
    session_key = get_session_key(request)
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.session_key = session_key
            place.save()
            return redirect("places_to_go:places_list")
    else:
        form = PlaceForm()
    return render(request, "places_to_go/add_place.html", {"form": form})
