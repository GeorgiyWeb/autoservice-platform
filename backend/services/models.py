from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_min = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    
class Master(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    specialization = models.CharField(max_length=200)
    services = models.ManyToManyField(Service, related_name='masters', blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['last_name', 'first_name']
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
     
    
