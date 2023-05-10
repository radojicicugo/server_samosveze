from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Podaci(models.Model):
    product = models.CharField(max_length=25, null=True, blank=False)
    image = models.ImageField(upload_to='uploads/images', null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=False)
    email = models.EmailField(max_length=50, null=True, blank=False)
    description = models.CharField(max_length=500, null=True, blank=False)
    klass = models.CharField(max_length=1, null=True, blank=False)
    price = models.CharField(max_length=10, null=True, blank=False)
    phone = models.CharField(max_length=15, null=True, blank=False)
           
    def __str__(self):
        return self.product or ' '