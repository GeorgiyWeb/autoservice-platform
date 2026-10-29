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
        read_only_fields = ['price', 'client']
        
    def validate(self, attrs):
        master = attrs["master"]
        date = attrs["date"]
        start_time = attrs["start_time"]
        end_time = attrs["end_time"]
        
        conflicts = Booking.objects.filter(master=master, date=date, start_time__lt=end_time, end_time__gt=start_time)
        
        if conflicts.exists():
            raise serializers.ValidationError("This time slot is already booked.")
        
        return attrs