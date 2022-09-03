from django.urls import path
from sales import views
urlpatterns = [
  
  path('quotations/list',views.QuotationView.as_view(),name='q-list'),
  # path('quotations/new/',views.CreateQuotationView.as_view(),name='new-quote'),
  path('quotations/new/',views.quotation_create_view,name='new-quote'),
  path('customers/new/',views.customer_create_view,name='new-customer'),
  path('customers/list/',views.customers_list,name='customers-list'),
  path('invoices/list/',views.invoices_list,name='invoices-list'),
  path('invoices/new/',views.create_invoice,name='new-invoice'),
  path('delivery/new/',views.create_delivery,name='new-delivery'),
  path('delivery/list/',views.delivery,name='delivery-list'),
 
  path('credit_notes/list/',views.credit_notes,name='credit_notes'),
  
]