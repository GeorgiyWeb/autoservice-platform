from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import timedelta, datetime, time

from .models import Service, Master, Booking
from users.models import Autoservice
from .serializers import ServiceSerializer, MasterSerializer, BookingSerializer


# Create your views here.

class ServicePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100 # DoS protection:  prevents huge page_size requests


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_active', 'price', 'autoservice']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'duration_min']
    pagination_class = ServicePagination
    
    def perform_create(self, serializer):
        autoservice = Autoservice.objects.get(owner=self.request.user)
        serializer.save(autoservice=autoservice)
    
    def get_queryset(self):
        user = self.request.user
        
        if not user.is_authenticated:
            return Service.objects.all()
        
        if user.profile.role == "owner":
            try:
                autoservice = Autoservice.objects.get(owner=user)
                return Service.objects.filter(autoservice=autoservice)
            except Autoservice.DoesNotExist:
                return Service.objects.none()
            
        return Service.objects.all()

class MasterViewSet(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_active', 'specialization', 'autoservice']
    ordering_fields = ['first_name', 'last_name', 'created_at']
    search_fields = ['first_name', 'last_name', 'specialization']
    pagination_class = ServicePagination
    
    def perform_create(self, serializer):
        autoservice = Autoservice.objects.get(owner=self.request.user)
        serializer.save(autoservice=autoservice)
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['date', 'status']
    ordering_fields = ['created_at', 'date', 'start_time']
    pagination_class = ServicePagination
    
    def get_queryset(self):
        user = self.request.user
        
        if not user.is_authenticated:
                return Booking.objects.none()
            
        role = user.profile.role
        
        if role == "owner":
            return Booking.objects.all()
        elif role == "client":
            return Booking.objects.filter(client=user)
    
    
    def perform_create(self, serializer):
        autoservice = Autoservice.objects.get(owner=self.request.user)
        serializer.save(client=self.request.user, autoservice=autoservice)

        

    @action(detail=False, methods=["get"])
    def slots(self, request):
        master_id = request.query_params.get('master_id')
        date = request.query_params.get('date')
        service_id = request.query_params.get('service_id') 

        
        if not master_id or not date or not service_id:
            return Response({"error": "master_id, date and service_id are required"}, status=400)

       
        service = Service.objects.get(id=service_id)
        duration = service.duration_min

     
        bookings = Booking.objects.filter(master_id=master_id, date=date)

       
        start_of_day = datetime.combine(datetime.strptime(date, "%Y-%m-%d").date(), time(9, 0))
        end_of_day = datetime.combine(datetime.strptime(date, "%Y-%m-%d").date(), time(18, 0))
        step = timedelta(minutes=30)
        
        available_slots = []
        current_time = start_of_day

      
        while current_time + timedelta(minutes=duration) <= end_of_day:
            is_free = True
            
            for b in bookings:
                if current_time.time() < b.end_time and (current_time + timedelta(minutes=duration)).time() > b.start_time:
                    is_free = False
                    break
            
            if is_free:
                available_slots.append(current_time.strftime("%H:%M"))
 
            current_time += step

        return Response({"date": date, "available_slots": available_slots})
    
    
    
    