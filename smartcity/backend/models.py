from django.db import models
from django.utils import timezone

CONTINENTS = [
    ('Africa','Africa'),
    ('Europe','Europe'),
    ('Asia','Asia'),
]
# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}'

class Category(models.Model):
    name = models.CharField(max_length=50)
    services = models.ForeignKey(Service, on_delete=models.CASCADE)
    document_required = models.BooleanField(default=False)

class Country(models.Model):
    name = models.CharField(max_length=50)
    continent = models.CharField(choices=CONTINENTS, max_length=20)

    def __str__(self):
        return f'{self.name}'

class State(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class LocalGovernmentArea(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class ServiceProvider(models.Model):
    """Model for service providers"""
    name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    service_rendered = models.CharField(max_length=50)
    service_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=50)
    description = models.TextField(max_length=200)
    year_of_experience = models.IntegerField()
    year_of_establishement = models.DateField(default=timezone.now().date())
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    local_government_are = models.ForeignKey(LocalGovernmentArea, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    supporting_document = models.FileField()
    rating = models.FloatField()

    def __str__(self):
        return f'{self.name}'
    
    