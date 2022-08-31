from django.urls import path
from sales import views
urlpatterns = [
  path('quotations/list',views.QuotationView.as_view(),name='q-list'),
  # path('quotations/new/',views.CreateQuotationView.as_view(),name='new-quote'),
  path('quotations/new/',views.quotation_create_view,name='new-quote'),
  path('customers/new/',views.customer_create_view,name='new-customer'),
  path('customers/list/',views.customers_list,name='customers-list'),
  path('invoices/list/',views.invoices_list,name='invoices-list'),
  path('vendors/list/',views.vendors_list,name='vendors-list'),
  path('purchse/list/',views.purchase_orders_list,name='purchase-list'),
  path('vendors_credit/list/',views.vendor_credit,name='vendors-credit'),
  path('expenses/list/',views.expenses,name='expenses'),
  path('credit_notes/list/',views.credit_notes,name='credit_notes'),
  path('delivery/list/',views.delivery,name='delivery')
]