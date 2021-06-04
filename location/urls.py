from re import I
from django.urls import path
from .views import HotelUpdateRetreiveView, ListCreateGenericViews

urlpatterns = [
    path("hotels", ListCreateGenericViews.as_view()),
    path(
        "hotels/<str:pk>",
        HotelUpdateRetreiveView.as_view(),
    ),
]
