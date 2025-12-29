from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('sale/create/', create_sale_invoice, name='create_invoice'),
    path('sale/<int:invoice_id>/', invoice_detail, name='invoice_detail'),
    path('purchase/create/', create_purchase_invoice, name='create_purchase_invoice'),
    path('purchase/<int:invoice_id>/add-item/', add_purchase_item, name='add_purchase_item'),
    path('payment/add/', add_payment, name='add_payment'),
    path('reports/customers/', customers_report, name='customers_report'),
    path('reports/open-invoices/', open_invoices, name='open_invoices'),
    path('dashboard/', dashboard, name='dashboard'),


    path('inventory/', inventory, name='inventory'),
]
