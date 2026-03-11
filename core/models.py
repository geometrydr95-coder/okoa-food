from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    estate = models.CharField(max_length=100)  # e.g., Westlands, Kilimani
    category = models.CharField(max_length=50) # e.g., Bakery, Cafe
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.name

class SurpriseBag(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='bags')
    name = models.CharField(max_length=100, default="Surprise Bag")
    price_kes = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    pickup_start = models.TimeField()
    pickup_end = models.TimeField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} from {self.restaurant.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bag = models.ForeignKey(SurpriseBag, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Reserved')