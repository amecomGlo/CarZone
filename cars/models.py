from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify
from datetime import datetime
from django.urls import reverse
from multiselectfield import MultiSelectField
# Create your models here.
class Car(models.Model):
    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, unique=True)
    state = models.CharField(max_length=255, choices=state_choice)
    city = models.CharField(max_length=200)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'),choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    photo_1 = models.ImageField(upload_to='photo/%Y/%m/%d')
    photo_2 = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, null=True)
    photo_5 = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, null=True)
    features = MultiSelectField(choices=features_choices, max_choices=15,
                                 max_length=200)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(max_length=100)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.CharField(max_length=200)
    fuel_type = models.CharField(max_length=100)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product:detail", kwargs={"slug":self.slug})
    
    class Meta:
        ordering = ['-created_at']
    
def save_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug=new_slug
    obj = Car.objects.filter(slug=slug)
    exists = obj.exists()
    if exists:
        new_slug = "%s/%s"%(slug, obj.first().id)
        return save_slug(instance, new_slug=new_slug)
    return slug


def car_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug =  save_slug(instance)

pre_save.connect(car_pre_save_receiver, sender=Car)
    
