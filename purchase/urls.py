from django.urls import path
from purchase import views
urlpatterns = [
  

  path('vendors/list/',views.vendors_list,name='vendors-list'),
  path('vendors/new/',views.create_vendor,name='new-vendor'),
  path('purchase/list/',views.purchase_orders_list,name='purchase-list'),
  path('new/',views.create_purchase,name='new-purchase'),
  path('vendors_credit/list/',views.vendor_credit,name='vendors-credit'),
  path('expenses/list/',views.expenses,name='expenses'),
  
  
]