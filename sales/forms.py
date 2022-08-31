from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from django import forms
from sales.models import Customer, Customer_Address,Quotation,Quote_Items


class CustomerCreateForm(ModelForm):   
    class Meta:
        model=Customer
        fields=[
            "company_name",
            "customer_displayname",
            "display_name_arabic",
            "cusotmer_email",
            "customer_phone",
            "buyer_id_options",
            "buyer_id"
        ]
        

class CustomerAddressForm(ModelForm):
    class Meta:
        model=Customer_Address
        exclude = ('customer',)

class Quote_form(ModelForm):
    class Meta:
        model=Quotation
        fields=["customer_name","quote_expdate","customer_notes","terms_and_conditions"]   

class Quoteitem_form(ModelForm):
    class Meta:
        model=Quote_Items
        fields="__all__"