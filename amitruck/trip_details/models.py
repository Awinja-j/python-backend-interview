from django.db import models


class User(models.Model):
    USER_TYPE_CHOICES = [
        ('customer', 'Customer'),
        ('driver', 'Driver'),
        ('admin', 'Admin'),
    ]

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='customer')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    

class Trip(models.Model):
    address_type_choices = [
        ('pickup_point', 'Pickup Point'),
        ('drop_off_point', 'Drop Off Point')
    ]

    driver_id = models.IntegerField()
    vehicle_id = models.IntegerField()
    customer_id = models.IntegerField()
    address = models.CharField(max_length=50)
    cargo_tonnage = models.DecimalField(max_digits=10, decimal_places=2)
    address_type = models.CharField(max_length=15, choices=address_type_choices)
    done_by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Trip {self.id} - {self.address}"
    
class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=100)
    trips = models.ManyToManyField(Trip, related_name='vehicles')
    users = models.ManyToManyField(User, related_name='vehicles')

    def __str__(self):
        return self.vehicle_name
