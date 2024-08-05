from django.db import models
# from django.forms import forms
# from django import forms
from django.contrib.auth.models import User

from phone_field import PhoneField

# Create your models here.
class personal(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      first_name = models.CharField(max_length=50)
      lasrt_name = models.CharField(max_length=50)
      city = models.CharField(max_length=50)
      phone = PhoneField(blank=True, help_text='Contact phone number')
      email = models.EmailField(blank=True)
      

      def __str__(self):
            return f'{self.fname} {self.lname}'
      
