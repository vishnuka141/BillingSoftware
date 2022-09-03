from django.shortcuts import render

# Create your views here.
def vendors_list(request):
    return render(request,'vendors.html')    
def create_vendor(request):
    return render(request,'new_vendor.html')
def purchase_orders_list(request):
    return render(request,'purchase.html')
def create_purchase(request):
    return render(request,"new_purchase.html")
def vendor_credit(request):
    return render(request,'vendors_credit.html')
def expenses(request):
    return render(request,'expenses.html')