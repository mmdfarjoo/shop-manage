from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(SaleInvoice)
admin.site.register(SaleItem)
admin.site.register(PurchaseInvoice)
admin.site.register(PurchaseItem)
