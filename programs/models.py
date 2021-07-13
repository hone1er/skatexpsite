from django.db import models
from django.db.models.fields.reverse_related import ManyToManyRel, ManyToOneRel
from django.utils import timezone
from django import forms
from ckeditor.fields import RichTextField
from phone_field import PhoneField


# Create your models here.
class Program(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150, default='', blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    content = RichTextField(blank=True, null=True)


    def __str__(self):
        return self.title


class Customer(models.Model):
    parent = models.CharField(max_length=100)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    parent_email = models.EmailField(max_length=254)
    student = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=254)
    student_phone = PhoneField(blank=True, help_text='Student phone number')
    student_grade = models.CharField(max_length=20)
    student_address = models.CharField(max_length=254)

    def __str__(self):
        return self.student
