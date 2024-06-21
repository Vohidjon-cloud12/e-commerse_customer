from django import forms

from app.models import Product, Customers


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ()


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customers
        exclude = ()
