from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_control
from django.views.generic import TemplateView,FormView,CreateView
from accounts.views import signin_required_user
from django.utils.decorators import method_decorator
from accounts.models import CustomUser
from sales.models import Customer,Customer_Address
from sales.forms import CustomerCreateForm,CustomerAddressForm
# from sales.models import


# Create your views here.
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@method_decorator(signin_required_user,name="dispatch")
class QuotationView(TemplateView):
    template_name = 'quotations.html'


class CreateQuotationView(TemplateView):
    template_name='quotation-form.html'
    
def customer_create_view(request,**kwargs):
    
    if request.method=="POST":
        form=CustomerCreateForm(request.POST)       
        if form.is_valid():
            form.instance.created_user=request.user
            form.save()
            return redirect('new-quote')
    else:
         form=CustomerCreateForm()
         print(form)
    return render(request,'new-customer.html',{"form":form})

def quotationformview(request):
    
    # context = {}
    customers = Customer.objects.filter(created_user=request.user)

    # form=QuotationForm(request.POST)
    # if form.is_valid():
    #     form.save()
    #     return redirect('q-list')
    # context['form'] = form
    return render(request,'quotation-form.html', {"customers":customers})







