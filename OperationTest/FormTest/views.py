from django.shortcuts import redirect, render
from .models import Item
from .forms import ItemForm
from datetime import datetime
from django.http import HttpResponseRedirect

# Create your views here.

#all Items view
def allItems(request):

   item_list=Item.objects.all()
   return render(request,'formTest/allItems.html',context={'item_list':item_list})

#add Items view
def addItem(request):
    submitted= False
    if request.method == "POST":
        form=ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')

    else:
        form =ItemForm
        if 'submitted' in request.GET:
            submitted= True

    form=ItemForm
    return render(request,'formTest/add-Item.html',context={'form':form, 'submitted':submitted})

#update items view
def updateItem(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('allItems')

    return render(request,'formTest/update-Item.html',context={'item':item,'form':form})

#items to be updated view
def toBeUpdated(request):
   itemToBeUpdated=Item.objects.all()
   return render(request,'formTest/items_toBeUpdated.html',context={'itemToBeUpdated': itemToBeUpdated})

#delete items view
def deleteItem(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    return redirect('allItems')