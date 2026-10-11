from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Service
from .serializers import ServiceSerializer


# Create your views here.

class ServicePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_active', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'duration_min']
    pagination_class = ServicePagination
    
    