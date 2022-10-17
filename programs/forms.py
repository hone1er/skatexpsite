from django.db.models import fields
from django.forms import ModelForm
from .models import Coupon, Hotdogger, PeProgram, forms, VanTour, PhoneField


class HotdoggerForm(ModelForm):
    class Meta:
        model = Hotdogger
        fields = "__all__"
        exclude = ("created_at", "coupon")
        widgets = {
            "parent": forms.TextInput(attrs={"placeholder": "Parent Name"}),
            "phone": PhoneField(help_text="Contact Phone Number"),
            "parent_email": forms.EmailInput(attrs={"placeholder": "Parent Email"}),
            "skater": forms.TextInput(attrs={"placeholder": "Skater Name"}),
            "month_or_event": forms.TextInput(attrs={"placeholder": "Month or Event"}),
            "emergency_contact": forms.TextInput(
                attrs={"placeholder": "Emergency Contact Name"}
            ),
            "emergency_contact_phone": PhoneField(
                help_text="Emergency Contact Phone",
            ),
        }


class VanTourForm(ModelForm):
    class Meta:
        model = VanTour
        fields = "__all__"
        exclude = ("created_at", "coupon")
        widgets = {
            "parent": forms.TextInput(attrs={"placeholder": "Parent Name"}),
            "phone": PhoneField(help_text="Contact Phone Number"),
            "parent_email": forms.EmailInput(attrs={"placeholder": "Parent Email"}),
            "skater": forms.TextInput(attrs={"placeholder": "Skater Name"}),
            "month_or_event": forms.TextInput(attrs={"placeholder": "Month or Event"}),
            "emergency_contact": forms.TextInput(
                attrs={"placeholder": "Emergency Contact Name"}
            ),
            "emergency_contact_phone": PhoneField(
                help_text="Emergency Contact Phone",
            ),
        }


class PeWaiver(ModelForm):
    food_program = forms.CheckboxInput()

    class Meta:
        model = PeProgram
        fields = "__all__"
        exclude = ("created_at", "coupon")
        widgets = {
            "parent": forms.TextInput(attrs={"placeholder": "Parent's Name"}),
            "phone": PhoneField(help_text="Contact Phone Number(required"),
            "parent_email": forms.EmailInput(attrs={"placeholder": "Parent Email"}),
            "parent_address": forms.TextInput(attrs={"placeholder": "Parent Address"}),
            "skater": forms.TextInput(attrs={"placeholder": "Skater's Full Name"}),
            "skater_email": forms.EmailInput(attrs={"placeholder": "Skater Email"}),
            "skater_phone": PhoneField(
                help_text="Skater Phone Number",
            ),
            "skater_grade": forms.TextInput(attrs={"placeholder": "Skater Grade"}),
            "skater_school_number": forms.TextInput(
                attrs={"placeholder": "Skater School Number"}
            ),
            "slc_number": forms.TextInput(attrs={"placeholder": "SLC Number"}),
            "food_program": forms.CheckboxInput(),
        }
