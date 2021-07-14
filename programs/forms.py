from django.db.models import fields
from django.forms import ModelForm
from .models import Customer, forms, PhoneField

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'parent' : forms.TextInput(attrs = {'placeholder': 'Parent Name'}),
            'phone' : PhoneField(blank=True),
            'parent_email' : forms.EmailInput(attrs = {'placeholder': 'Parent Email'}),
            'student' : forms.TextInput(attrs = {'placeholder': 'Student'}),
            'student_email' : forms.EmailInput(attrs = {'placeholder': 'Student Email'}),
            'student_phone' : PhoneField(blank=True),
            'student_grade' : forms.TextInput(attrs = {'placeholder': 'Student Grade'}),
            'student_address' : forms.TextInput(attrs = {'placeholder': 'Student Address'}),
        }