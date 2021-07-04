from location.serializers import HotelSerializer
from django.shortcuts import render
from rest_framework import generics
from .models import Hotel

from django.contrib.gis.geos import Point
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="location")


class ListCreateGenericViews(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def perform_create(self, serializer):
        street_1 = serializer.initial_data["street_1"]
        address = serializer.initial_data["city"]
        state = serializer.initial_data["state"]
        country = serializer.initial_data["city"]
        data = [street_1, address, state, country]
        " ".join(data)

        g = geolocator.geocode(data)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        print(pnt)
        serializer.save(location=pnt)


class HotelUpdateRetreiveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def perform_update(self, serializer):
        street_1 = serializer.initial_data["street_1"]
        address = serializer.initial_data["city"]
        state = serializer.initial_data["state"]
        country = serializer.initial_data["city"]
        data = [street_1, address, state, country]
        " ".join(data)

        g = geolocator.geocode(data)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        print(pnt)
        serializer.save(location=pnt)
