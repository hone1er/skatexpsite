from programs.models import Program
from django.contrib import admin
from .models import Customer, Program

# Register your models here.
admin.site.register(Program)
admin.site.register(Customer)