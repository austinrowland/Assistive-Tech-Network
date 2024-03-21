from django.db import models

# Create your models here.
class Profile(models.Model): # User was already registered with admin
    username = models.CharField(max_length=128)
    display_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=200)
    date_joined = models.DateTimeField("Date joined")
    # May eventually link to posts that a user has made once we get that model

    def __str__(self):
        return self.username

class Organization(models.Model):
    display_name = models.CharField(max_length=128)
    affiliated_users = models.ManyToManyField(Profile)
    
    def __str__(self):
        return self.display_name

class Product(models.Model):
    display_name = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.display_name