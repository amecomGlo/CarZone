from django.db import models
from datetime import datetime
from cars.models import Car
# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    car_slug = models.SlugField(blank=True, null=True)
    customer_need = models.CharField(max_length=255)
    car_title = models.CharField(max_length=255)
    car_price = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __strt__(self):
        return self.first_name