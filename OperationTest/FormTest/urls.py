from django.urls import path
from . import views

urlpatterns = [
    path('',views.addItem,name='add-Item'),
    path('allItems',views.allItems, name='allItems'),
    path('update-Item/<item_id>',views.updateItem,name='update-Item'),
    path('items_toBeUpdated',views.toBeUpdated, name='items_toBeUpdated'),
    path('delete-Item/<item_id>',views.deleteItem,name='delete-Item')
]
