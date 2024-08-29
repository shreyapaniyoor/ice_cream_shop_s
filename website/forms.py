from django import forms

from .models import Product, Enquiry, Contact

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['first_name', 'last_name', 'email', 'mobile', 'product', 'message']

    user = forms.CharField(required=False)

    product = forms.ModelChoiceField(
        queryset=Product.objects.filter(),
        empty_label='Select Product',
        to_field_name='id'
    )

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']