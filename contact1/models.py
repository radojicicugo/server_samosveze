from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Contact1(models.Model):
    message = models.CharField(max_length=300, null=True, blank=False)
    name = models.CharField(max_length=50, null=True, blank=False)
    email = models.EmailField(max_length=50, null=True, blank=False)
           
    def __str__(self):
        return self.name or ' '