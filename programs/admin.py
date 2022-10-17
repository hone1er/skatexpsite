from programs.models import Program
from django.contrib import admin
from .models import Hotdogger, Program, PeProgram, VanTour, Coupon

# Register your models here.
admin.site.register(Program)
admin.site.register(Hotdogger)
admin.site.register(PeProgram)
admin.site.register(VanTour)
admin.site.register(Coupon)
