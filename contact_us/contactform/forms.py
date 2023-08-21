from django import forms
from .models import contactform

select_mode_of_contact = (
    ("email", "E-Mail"),
    ("phone", "Phone"),
)


class ContactForm(forms.ModelForm):
    phone = forms.CharField(required=False)
    mode_of_contact = forms.CharField(required=False, widget=forms.RadioSelect(choices=select_mode_of_contact))
    
    class Meta:
        model = contactform
        fields = '__all__'