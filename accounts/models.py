from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Administrador/Socio'),
        ('WAITER', 'Mesero'),
        ('CASHIER', 'Cajero'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='ADMIN')
    phone = models.CharField(max_length=20, blank=True, null=True)
    assigned_business = models.ForeignKey('business.Business', on_delete=models.SET_NULL, null=True, blank=True, related_name='staff')

    def __str__(self):
        role_label = self.get_role_display() if self.role else "General"
        return f"{self.username} ({role_label})"
