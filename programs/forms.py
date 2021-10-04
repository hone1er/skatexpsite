from django.db.models import fields
from django.forms import ModelForm
from .models import Coupon, Hotdogger, PeProgram, forms, PhoneField


class HotdoggerForm(ModelForm):
    class Meta:
        model = Hotdogger
        fields = "__all__"
        exclude = ("created_at", "coupon")
        widgets = {
            "parent": forms.TextInput(attrs={"placeholder": "Parent Name"}),
            "phone": PhoneField(blank=True, help_text="Contact phone number"),
            "parent_email": forms.EmailInput(attrs={"placeholder": "Parent Email"}),
            "parent_address": forms.TextInput(
                attrs={"placeholder": "skater Address"}
            ),
            "skater": forms.TextInput(attrs={"placeholder": "skater"}),
            "skater_email": forms.EmailInput(attrs={"placeholder": "skater Email"}),
            "skater_phone": PhoneField(blank=True, help_text="skater phone number"),
            "skater_grade": forms.TextInput(attrs={"placeholder": "skater Grade"}),
            "school": forms.TextInput(attrs={"placeholder": "School"}),
        }


class PeWaiver(ModelForm):
    food_program = forms.CheckboxInput()
    class Meta:
        model = PeProgram
        fields = "__all__"
        exclude = ("created_at", "coupon")
        widgets = {
            "parent": forms.TextInput(attrs={"placeholder": "Parent Name"}),
            "phone": PhoneField(blank=True, help_text="Contact phone number"),
            "parent_email": forms.EmailInput(attrs={"placeholder": "Parent Email"}),
            "parent_address": forms.TextInput(
                attrs={"placeholder": "skater Address"}
            ),
            "skater": forms.TextInput(attrs={"placeholder": "skater"}),
            "skater_email": forms.EmailInput(attrs={"placeholder": "skater Email"}),
            "skater_phone": PhoneField(blank=True, help_text="skater phone number"),
            "skater_grade": forms.TextInput(attrs={"placeholder": "skater Grade"}),
            "skater_id": forms.TextInput(attrs={"placeholder": "skater ID"}),
            "food_program": forms.CheckboxInput(),
            
        }




