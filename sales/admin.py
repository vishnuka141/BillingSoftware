from django.contrib import admin
from sales.models import Customer,Customer_Address,Quotation,Quote_Items
# Register your models here.

admin.site.register(Customer)
admin.site.register(Customer_Address)
admin.site.register(Quotation)