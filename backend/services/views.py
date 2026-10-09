from rest_framework import viewsets
from .serializers import ServiceSerializer
from .models import Service

# Create your views here.

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer