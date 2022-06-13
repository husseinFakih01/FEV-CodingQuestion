from django import forms
from django.forms import BooleanField, ModelForm
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model=Item
        fields = ('name', 'price', 'quantity', 'description')
        labels= {
            'name':'',
            'price':'',
            'quantity':'',
            'description':''
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','PlaceHolder': 'Name'}),
            'price':forms.NumberInput(attrs={'class':'form-control','PlaceHolder': 'Price'}),
            'quantity':forms.TextInput(attrs={'class':'form-control','PlaceHolder': 'Quantity'}),
            'description':forms.Textarea(attrs={'class':'form-control','PlaceHolder': 'Description'}),
        }