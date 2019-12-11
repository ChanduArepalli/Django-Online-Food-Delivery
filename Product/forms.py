from django import forms
from .models import Product, Order



class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control',})
        self.fields['contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['count'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control',})
    class Meta:
        model = Order
        fields = ['count', 'name','contact','address', ]

