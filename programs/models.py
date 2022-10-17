from django.db import models
from django.db.models.fields.reverse_related import ManyToManyRel, ManyToOneRel
from django.utils import timezone
from django import forms
from ckeditor.fields import RichTextField
from phone_field import PhoneField


# Create your models here.
class Program(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150, default="", blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    content = RichTextField(blank=True, null=True)
    stripe_id = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return str(self.title)


class Hotdogger(models.Model):
    parent = models.CharField(max_length=100)
    phone = PhoneField()
    parent_email = models.EmailField(max_length=254)
    skater = models.CharField(max_length=100)
    month_or_event = models.CharField(max_length=254)
    emergency_contact = models.CharField(blank=True, max_length=254)
    emergency_contact_phone = PhoneField(blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return str(self.skater)


class VanTour(models.Model):
    parent = models.CharField(max_length=105)
    phone = PhoneField()
    parent_email = models.EmailField(max_length=254)
    skater = models.CharField(max_length=100)
    month_or_event = models.CharField(max_length=254)
    emergency_contact = models.CharField(blank=True, max_length=254)
    emergency_contact_phone = PhoneField(blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return str(self.skater)


class PeProgram(models.Model):
    parent = models.CharField(max_length=100)
    phone = PhoneField()
    parent_email = models.EmailField(max_length=254)
    parent_address = models.CharField(max_length=254)
    skater = models.CharField(max_length=100)
    skater_email = models.EmailField(max_length=254)
    skater_phone = PhoneField()
    skater_grade = models.CharField(max_length=20)
    skater_school_number = models.CharField(max_length=254)
    slc_number = models.CharField(max_length=254)
    food_program = models.BooleanField(
        verbose_name="Payment Assistance",
        help_text="**Only check this box if you are enrolled in the free lunch program. We will need to verify enrollement or full price will be charged at the end of the semester.",
        blank=True,
    )
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return str(self.skater)


class Coupon(models.Model):
    code = models.CharField(max_length=100, blank=True)
    amount_off = models.DecimalField(max_digits=6, decimal_places=2, blank=True)

    def __str__(self):
        return str(self.code)
