import imp
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def admin_console(render):
    products = Product.objects.all()
    return render(request, 'products/products_page.html', ('products': products))