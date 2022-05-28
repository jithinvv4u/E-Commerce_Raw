from django import forms
from .models import Cart, Item

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields='__all__'

class CartForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields='__all__'