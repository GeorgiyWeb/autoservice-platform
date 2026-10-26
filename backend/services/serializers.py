from rest_framework import serializers
from .models import Service, Master, Booking


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price', 'duration_min', 'is_active']


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'bio', 'specialization', 'services', 'is_active']
        

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'client', 'service', 'master', 'date', 'start_time', 'end_time', 'price', 'status']
        read_only_fields = ['price']