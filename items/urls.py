from django.urls import path
from items import views
urlpatterns = [
  path('item/list/',views.item_list,name='item-list'),
  path('items/add/',views.add_items,name='add-item')

]