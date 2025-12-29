from django import forms
from .models import SaleInvoice, SaleItem , PurchaseInvoice, PurchaseItem , Payment


class SaleInvoiceForm(forms.ModelForm):
    class Meta:
        model = SaleInvoice
        fields = ['customer']


class SaleItemForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = ['product', 'quantity', 'price']


class PurchaseInvoiceForm(forms.ModelForm):
    class Meta:
        model = PurchaseInvoice
        fields = ['supplier_name']


class PurchaseItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = ['product', 'quantity', 'price']



class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['customer', 'amount', 'description']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['customer', 'invoice', 'amount', 'description']
