from django.shortcuts import render, redirect, get_object_or_404
from .models import SaleInvoice, Product, Customer, Payment
from .forms import SaleInvoiceForm, SaleItemForm , PurchaseInvoiceForm , PurchaseInvoice , PurchaseItemForm , PaymentForm , CustomerForm ,PurchaseItem
from django.db.models import Sum
from django.utils.timezone import now

def home(request):
    return render(request, 'home.html')


def create_sale_invoice(request):
    invoice = None

    if request.method == 'POST':
        invoice_form = SaleInvoiceForm(request.POST)
        item_form = SaleItemForm(request.POST)

        if invoice_form.is_valid() and item_form.is_valid():
            invoice = invoice_form.save()
            item = item_form.save(commit=False)
            item.invoice = invoice
            item.save()

            return redirect('invoice_detail', invoice.id)
    else:
        invoice_form = SaleInvoiceForm()
        item_form = SaleItemForm()

    return render(request, 'sale/create_invoice.html', {
        'invoice_form': invoice_form,
        'item_form': item_form
    })


def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(SaleInvoice, id=invoice_id)
    return render(request, 'sale/invoice_detail.html', {
        'invoice': invoice
    })



def create_purchase_invoice(request):
    if request.method == 'POST':
        form = PurchaseInvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save()
            return redirect('add_purchase_item', invoice.id)
    else:
        form = PurchaseInvoiceForm()

    return render(request, 'purchase/create_invoice.html', {
        'form': form
    })

def add_purchase_item(request, invoice_id):
    invoice = get_object_or_404(PurchaseInvoice, id=invoice_id)

    if request.method == 'POST':
        form = PurchaseItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.invoice = invoice
            item.save()
            return redirect('add_purchase_item', invoice.id)
    else:
        form = PurchaseItemForm()

    return render(request, 'purchase/add_item.html', {
        'invoice': invoice,
        'form': form
    })



def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers_report')
    else:
        form = PaymentForm()

    return render(request, 'payment/add_payment.html', {
        'form': form
    })


def customers_report(request):
    customers = Customer.objects.all()
    return render(request, 'reports/customers.html', {
        'customers': customers
    })


def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('open_invoices')
    else:
        form = PaymentForm()

    return render(request, 'payment/add_payment.html', {
        'form': form
    })

def open_invoices(request):
    invoices = SaleInvoice.objects.all()
    open_invoices = [i for i in invoices if i.remaining_amount() > 0]

    return render(request, 'reports/open_invoices.html', {
        'invoices': open_invoices
    })




def dashboard(request):
    invoices = SaleInvoice.objects.all()
    payments = Payment.objects.all()

    total_sales = sum(i.total_price() for i in invoices)
    total_paid = sum(p.amount for p in payments)
    total_debt = total_sales - total_paid

    open_invoices_count = len(
        [i for i in invoices if i.remaining_amount() > 0]
    )

    low_stock_products = Product.objects.filter(stock__lte=5)

    recent_invoices = SaleInvoice.objects.order_by('-date')[:5]
    recent_payments = Payment.objects.order_by('-date')[:5]

    context = {
        'total_sales': total_sales,
        'total_paid': total_paid,
        'total_debt': total_debt,
        'open_invoices_count': open_invoices_count,
        'low_stock_products': low_stock_products,
        'recent_invoices': recent_invoices,
        'recent_payments': recent_payments,
    }

    return render(request, 'dashboard/dashboard.html', context)






from .models import Product

def inventory(request):
    products = Product.objects.all()
    return render(request, 'inventory.html', {
        'products': products
    })



def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers_report')  # یا هر صفحه‌ای که میخوای بعد از ثبت بروه
    else:
        form = CustomerForm()

    context = {
        'form': form
    }
    return render(request, 'customer/add_customer.html', context)




def purchase_report(request):
    # همه کالاهایی که خریداری شده‌اند
    purchased_items = PurchaseItem.objects.select_related('product', 'invoice').all()

    # برای جمع‌بندی بر اساس محصول
    report = {}
    for item in purchased_items:
        prod = item.product
        if prod.id not in report:
            report[prod.id] = {
                'name': prod.name,
                'category': prod.category.name,
                'total_quantity': 0,
                'total_spent': 0
            }
        report[prod.id]['total_quantity'] += item.quantity
        report[prod.id]['total_spent'] += item.total_price()

    return render(request, 'purchase/purchase_report.html', {'report': report.values()})