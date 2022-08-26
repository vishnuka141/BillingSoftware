from django.urls import path
from sales import views
urlpatterns = [
  path('quotations/list',views.QuotationView.as_view(),name='q-list'),
  path('quotations/new/',views.CreateQuotationView.as_view(),name='new-quote'),
  path('customers/new/',views.customer_create_view,name='new-customer'),
]