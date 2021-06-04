from functools import partial
from re import search
from location.serializers import HotelSerializer
from django.shortcuts import render
from rest_framework import viewsets, exceptions, status
from rest_framework.response import Response
from .models import Hotel


class HotelViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = HotelSerializer(Hotel.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = HotelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        hotel = Hotel.objects.get(pk=pk)
        seriailizer = HotelSerializer(hotel)
        return Response(seriailizer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        hotel = Hotel.objects.get(pk=pk)
        serializer = HotelSerializer(instance=hotel, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        hotel = Hotel.objects.get(pk=pk)
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
