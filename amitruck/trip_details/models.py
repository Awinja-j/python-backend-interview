from django.db import models

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
    done_by_user_id = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
