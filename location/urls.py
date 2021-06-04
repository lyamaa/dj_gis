from re import I
from django.urls import path
from .views import HotelViewSet

urlpatterns = [
    path("hotels", HotelViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "hotels/<str:pk>",
        HotelViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
]
