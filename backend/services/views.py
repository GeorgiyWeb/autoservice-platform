from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Service
from .serializers import ServiceSerializer


# Create your views here.

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_active', 'price']
    
    