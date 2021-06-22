# make sure this is at the top if it isn't already
from django import forms
from phonenumber_field.modelfields import PhoneNumberField
# our new form
class ContactForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder' :'First name', 'style': 'width: 275px;'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder' :'Last name', 'style': 'width: 275px;'}))
    contact_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 275px;'}))
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder' :'Phone number (optional)', 'style': 'width: 275px;'}), required=False)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder' :'Your message', 'class': 'textarea', 'style': 'width: 560px;'})
    )