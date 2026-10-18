from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    ROLE_CHOICES = (
        ('owner', 'Owner'),
        ('master', 'Master'),
        ('client', 'Client'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    
    