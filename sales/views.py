from ast import Not
from multiprocessing import context
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_control
from django.views.generic import TemplateView,FormView,CreateView
from accounts.views import signin_required_user
from django.utils.decorators import method_decorator
from accounts.models import CustomUser
from sales.models import Customer,Customer_Address
from sales.forms import CustomerCreateForm,CustomerAddressForm,Quote_form,Quoteitem_form
# from sales.models import


# Create your views here.
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@method_decorator(signin_required_user,name="dispatch")
class QuotationView(TemplateView):
    template_name = 'quotations.html'


class CreateQuotationView(TemplateView):
    template_name='quotation-form.html'

    def get(self,request,**kwargs):
        customers = Customer.objects.filter(created_user=request.user)
        # customer=[cus for cus in customers]
        # print("hello",customer)
        
        context = {"quoteform":Quote_form(),"quoteitem_form":Quoteitem_form(),"customers":customers}
        
        return render(request,self.template_name,context)

    def post(self,request,**kwargs):
        
        
        quote_form= Quote_form(request.POST)
        quoteitem_form=Quoteitem_form(request.POST)
        if quote_form.is_valid() and quoteitem_form.is_valid():
            
            
            quote_form.instance.quote_createdby=customer
            quotation=quote_form.save()  


            data=quoteitem_form.save(commit=False)
            data.quotation= quotation
            data.save()
            return redirect("q-list")
        else:
            customers = Customer.objects.filter(created_user=request.user)
            context = {"quoteform":Quote_form(),"quoteitem_form":Quoteitem_form(),"customers":customers}
            return render(request,self.template_name,context)
             
    
def quotation_create_view(request):
    
    if request.method=="POST":
        customers = Customer.objects.filter(created_user=request.user)
        quote_form= Quote_form(request.POST)
        quoteitem_form=Quoteitem_form(request.POST)
        
        if quote_form.is_valid() and quoteitem_form.is_valid():
            customer_name=quote_form.cleaned_data.get("customer_name")
            quote_form.instance.quote_createdby=customer_name
            quote_form.save()   
        return redirect('q-list')
    else:
        customers = Customer.objects.filter(created_user=request.user)
        context = {"quoteform":Quote_form(),"quoteitem_form":Quoteitem_form(),"customers":customers}
        return render(request,'create_quotation.html',context)

def customer_create_view(request,**kwargs):
    
    if request.method=="POST":
        customercreate_form=CustomerCreateForm(request.POST)       
        customeraddress_form=CustomerAddressForm(request.POST)
        
        if customercreate_form.is_valid() and customeraddress_form.is_valid():
            customercreate_form.instance.created_user=request.user
            customer=customercreate_form.save()
           
            data=customeraddress_form.save(commit=False)
            data.customer=customer
            data.save()

        return redirect("new-quote")
    else:
        context={"customercreate_form":CustomerCreateForm(),"customeraddress_form":CustomerAddressForm()}
        return render(request,'new-customer.html',context)




def customers_list(request):
    return render(request,'customers.html')

def invoices_list(request):
    return render(request,'invoices.html')
def create_invoice(request):
    return render(request,'create_invoice.html')

def delivery(request):
    return render(request,'delivery.html')
def create_delivery(request):
    return render(request,'create_delivery.html')


def credit_notes(request):
    return render(request,'credit_notes.html')
def create_credit_notes(request):
    return render(request,'create_credit_note.html')







