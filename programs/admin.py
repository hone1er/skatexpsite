from programs.models import Program
from django.contrib import admin
from .models import Hotdogger, Program, PeProgram, Coupon

# Register your models here.
admin.site.register(Program)
admin.site.register(Hotdogger)
admin.site.register(PeProgram)
admin.site.register(Coupon)

