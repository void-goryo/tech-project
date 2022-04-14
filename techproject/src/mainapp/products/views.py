import imp
from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from django.http import HttpResponse
from . import views
from .forms import ProductForm
from .models import Product

def admin_console(request):
    products = Product.objects.all()
    return render(request, 'products/products_page.html', {'products': products})

def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Product, pk=pk)
    form = ProductForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid() == 'POST':
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
    else:
        return render(request, 'products/present_product.html', {'form':form})

def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('admin_console')
    context = {'item': item,}
    return render(request, 'products/confirmDelete.html', context)
