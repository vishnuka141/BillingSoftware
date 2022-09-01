from django.shortcuts import render

# Create your views here.
def item_list(request):
    return render(request,'item_list.html')
def add_items(request):
    return render(request,'add_item.html')