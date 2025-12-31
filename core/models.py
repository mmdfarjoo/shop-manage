from django.db import models
from django.core.exceptions import ValidationError




class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subs')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category} - {self.name}"

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    price = models.IntegerField()  # تومان
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name


#
#
# class Customer(models.Model):
#     name = models.CharField(max_length=200)
#     phone = models.CharField(max_length=15, blank=True)
#     address = models.TextField(blank=True)
#
#     def total_sales(self):
#         return sum(
#             invoice.total_price()
#             for invoice in self.saleinvoice_set.all()
#         )
#
#     def total_payments(self):
#         return sum(
#             payment.amount
#             for payment in self.payment_set.all()
#         )
#
#     def balance(self):
#         return self.total_sales() - self.total_payments()
#
#     def status(self):
#         if self.balance() > 0:
#             return "بدهکار"
#         elif self.balance() < 0:
#             return "بستانکار"
#         return "تسویه"
#
#     def __str__(self):
#         return self.name
#
#



class SaleInvoice(models.Model):
    customer = models.ForeignKey('core.Customer', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

    def paid_amount(self):
        return sum(payment.amount for payment in self.payments.all())

    def remaining_amount(self):
        return self.total_price() - self.paid_amount()

    def status(self):
        if self.remaining_amount() > 0:
            return "باز"
        return "تسویه"

    def __str__(self):
        return f"فاکتور {self.id}"



class SaleItem(models.Model):
    invoice = models.ForeignKey(
        SaleInvoice,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def total_price(self):
        return self.quantity * self.price

    def save(self, *args, **kwargs):
        if self.pk is None:  # فقط هنگام ایجاد
            if self.product.stock < self.quantity:
                raise ValidationError("موجودی کالا کافی نیست")

            # کاهش موجودی
            self.product.stock -= self.quantity
            self.product.save()

        super().save(*args, **kwargs)


class PurchaseInvoice(models.Model):
    supplier_name = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"حواله {self.id}"


class PurchaseItem(models.Model):
    invoice = models.ForeignKey(
        PurchaseInvoice,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def total_price(self):
        return self.quantity * self.price

    def save(self, *args, **kwargs):
        if self.pk is None:  # فقط هنگام ایجاد
            self.product.stock += self.quantity
            self.product.save()

        super().save(*args, **kwargs)


class Payment(models.Model):
    customer = models.ForeignKey('core.Customer', on_delete=models.CASCADE)
    invoice = models.ForeignKey(
        SaleInvoice,
        on_delete=models.CASCADE,
        related_name='payments',
        null=True,
        blank=True
    )
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.customer} - {self.amount}"




class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

