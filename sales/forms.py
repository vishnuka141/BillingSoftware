from django.forms import ModelForm
from django import forms
from sales.models import Customer, Customer_Address


class CustomerCreateForm(ModelForm):   
    class Meta:
        model=Customer
        fields=[
            "company_name",
            "customer_displayname",
            "display_name_arabic",
            "cusotmer_email",
            "customer_phone",
            "buyer_id",
        ]
        widgets={
            "company_name":forms.TextInput(attrs={"name":"company_name"}),
            "customer_displayname": forms.TextInput(attrs={"name": "customer_displayname"}),
            "display_name_arabic": forms.TextInput(attrs={"name": "display_name_arabic"}),
            "cusotmer_email": forms.EmailInput(attrs={"name": "cusotmer_email"}),
            "customer_phone": forms.TextInput(attrs={"name": "customer_phone"}),
            "buyer_id": forms.TextInput(attrs={"name": "buyer_id"}),            
        }

class CustomerAddressForm(ModelForm):
    class Meta:
        model=Customer_Address
        exclude = ('customer',)

        widgets={
            "country_or_region":forms.TextInput(attrs={"name":"country_or_region"}),
            "country_arabic": forms.TextInput(attrs={"name": "country_arabic"}),
            "building_number": forms.TextInput(attrs={"name": "building_number"}),
            "arabic_bdnumber": forms.TextInput(attrs={"name": "arabic_bdnumber"}),
            "street": forms.TextInput(attrs={"name": "street"}),
            "arabic_street": forms.TextInput(attrs={"name": "arabic_street"}),
            "city": forms.TextInput(attrs={"name": "city"}),
            "city_arabic": forms.TextInput(attrs={"name": "city_arabic"}),
            "zipcode": forms.TextInput(attrs={"name": "zipcode"}),
            "zipcode_arabic": forms.TextInput(attrs={"name": "zipcode_arabic"}),
            "phone_no": forms.TextInput(attrs={"name": "phone_no"})
        }