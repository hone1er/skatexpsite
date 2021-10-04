from django.db.models import fields
from django.forms import ModelForm
from .models import Coupon, Hotdogger, PeProgram, forms, PhoneField


class HotdoggerForm(ModelForm):
    class Meta:
        model = Hotdogger
        fields = "__all__"
        exclude = ("created_at", "coupon")
        widgets = {
            "parent": forms.TextInput(attrs={"placeholder": "Parent Name(required)"}),
            "phone": PhoneField(blank=True, help_text="Contact Phone Number"),
            "parent_email": forms.EmailInput(attrs={"placeholder": "Parent Email"}),
            "parent_address": forms.TextInput(
                attrs={"placeholder": "Parent Address"}
            ),
            "skater": forms.TextInput(attrs={"placeholder": "Skater Name(required)"}),
            "skater_email": forms.EmailInput(attrs={"placeholder": "Skater Email"}),
            "skater_phone": PhoneField(blank=True, help_text="Skater Phone Number"),
            "skater_grade": forms.TextInput(attrs={"placeholder": "Skater Grade"}),
            "school": forms.TextInput(attrs={"placeholder": "School"}),
        }


class PeWaiver(ModelForm):
    food_program = forms.CheckboxInput()
    class Meta:
        model = PeProgram
        fields = "__all__"
        exclude = ("created_at", "coupon")
        widgets = {
            "parent": forms.TextInput(attrs={"placeholder": "Parent Name(required)"}),
            "phone": PhoneField(blank=True, help_text="Contact Phone Number"),
            "parent_email": forms.EmailInput(attrs={"placeholder": "Parent Email"}),
            "parent_address": forms.TextInput(
                attrs={"placeholder": "Parent Address"}
            ),
            "skater": forms.TextInput(attrs={"placeholder": "Skater Name(required)"}),
            "skater_email": forms.EmailInput(attrs={"placeholder": "Skater Email"}),
            "skater_phone": PhoneField(blank=True, help_text="Skater Phone Number"),
            "skater_grade": forms.TextInput(attrs={"placeholder": "Skater Grade"}),
            "skater_id": forms.TextInput(attrs={"placeholder": "Skater ID"}),
            "food_program": forms.CheckboxInput(),
            
        }




