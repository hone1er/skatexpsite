from django.db import models
from django.db.models.fields.reverse_related import ManyToManyRel, ManyToOneRel
from django.utils import timezone
from django import forms

# Create your models here.
class Program(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.title

class SignUp(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.IntegerField()
