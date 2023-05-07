from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=120)
    twitter_link = models.URLField(max_length=120)
    google_plus_link = models.URLField(max_length=120)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self) -> str:
        return super(Team, self).__str__()
    
    

class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    message = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
