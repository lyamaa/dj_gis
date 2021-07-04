from location.models import Hotel
from rest_framework import serializers


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel

        fields = (
            "id",
            "name",
            "street_1",
            "street_2",
            "city",
            "state",
            "zip_code",
            "country",
            "location",
        )

        extra_kwargs = {"location": {"read_only": True}}
