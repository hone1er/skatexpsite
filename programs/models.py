from django.db import models
from django.db.models.fields.reverse_related import ManyToManyRel, ManyToOneRel
from django.utils import timezone
from django import forms
from ckeditor.fields import RichTextField


# Create your models here.
class Program(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = RichTextField(blank=True, null=True)


    def __str__(self):
        return self.title


