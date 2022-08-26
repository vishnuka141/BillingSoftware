
from django.db import models
from accounts.models import CustomUser
import datetime
from django.core.validators import MinValueValidator
# Create your models here.




buyer_options=(("NAT","NAT"),("TIN","TIN"),("IQA","IQA"),("PAS","PAS"),("CRN","CRN"),("MOM","MOM")
,("MLS","MLS"),("SAG","SAG"),("GCC","GCC"),("OTH","OTH")
)
class Customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    created_user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='created_user')
    company_name=models.CharField(max_length=250)
    customer_displayname=models.CharField(max_length=120)
    display_name_arabic=models.CharField(max_length=200,null=True)
    cusotmer_email=models.EmailField()
    customer_phone=models.CharField(max_length=120)
    buyer_id_options=models.CharField(choices=buyer_options,default='NAT',max_length=120)
    buyer_id=models.CharField(max_length=250)

    def __str__(self):
        return self.company_name


class Customer_Address(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,default=True,related_name='customer')
    country_or_region=models.CharField(max_length=120)
    country_arabic=models.CharField(max_length=120,null=True)
    building_number=models.CharField(max_length=120)
    arabic_bdnumber=models.CharField(max_length=120,null=True)
    street=models.CharField(max_length=120)
    arabic_street=models.CharField(max_length=120,null=True)
    city=models.CharField(max_length=120)
    city_arabic=models.CharField(max_length=250,null=True)
    zipcode=models.CharField(max_length=120)
    zipcode_arabic=models.CharField(max_length=120,null=True)
    phone_no=models.CharField(max_length=120)


    def __str__(self):
        return self.city

class Quote_Items(models.Model):
    item_id=models.AutoField(primary_key=True)
    item_details=models.CharField(max_length=120)
    quantity=models.PositiveIntegerField()
    rate=models.FloatField()
    discount=models.FloatField()
    tax=models.FloatField()
    amount=models.FloatField()

    def __str__(self):
        return self.item_id

class Quotation(models.Model):
    quote_createdby=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='quote_createdby')
    customer_name=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer_name')
    quote_id=models.AutoField(primary_key=True)
    quote_date=models.DateField(auto_now_add=True)
    quote_expdate=models.DateField()
    quote_items=models.ForeignKey(Quote_Items,on_delete=models.CASCADE,related_name="quote_items")
    quote_options = (
        ("pending", "pending"),
        ("approved", "approved"),
        ("cancelled", "cancelled"),
        ("expired", "expired")

    )
    quote_status=models.CharField(choices=quote_options, default='pending',max_length=120)
    customer_notes=models.TextField()
    terms_and_conditions=models.TextField()



    
