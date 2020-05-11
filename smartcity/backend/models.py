from django.db import models
from django.utils import timezone

# Create your models here.
class ServiceProvider(models.Model):
    """Model for service providers"""
    name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    service_rendered = models.CharField(max_length=50)
    service_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = ImageField(upload_to=None, height_field=None, width_field=None)
    description = models.TextField(max_length=200)
    year_of_experience = models.IntegerField()
    year_of_establishement = models.DateField(default=timezone.now().date())
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    local_government_are = models.ForeignKey(LocalGovernmentArea, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    supporting_document = models.FileField()
    rating = models.FloatField()

    def __str__(self):
        return f'{self.name}'
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    services = models.ForeignKey(Service, on_delete=models.CASCADE)
    document_required = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'
    