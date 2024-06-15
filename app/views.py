from django.shortcuts import render, redirect

from app.models import Product, Customer


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'app/index1.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'app/product-detail.html', context)


def customer_detail(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'app/customers.html',context)
