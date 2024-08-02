from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages





@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    orders_count = orders.count()
    products_count = products.count()
    workers_count = User.objects.all().count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders': orders,
        'form': form,
        'products': products,
        'products_count' : products_count,
        'orders_count' : orders_count,
        'workers_count' : workers_count,
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    orders_count = Order.objects.all().count
    products_count = Product.objects.all().count
    
    context = {
        'workers' :workers,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'products_count' : products_count,
    }
    return render(request, 'dashboard/staff.html', context)

@login_required(login_url='user-login')
def staff_detail(request, pk):
    worker = get_object_or_404(User, pk=pk)
    context = {
        'worker': worker,
        
    }
    return render(request, 'dashboard/staff_detail.html', context)

@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all()
    products = Product.objects.all()
    products_count = products.count()
    workers_count = User.objects.all().count
    orders_count = Order.objects.all().count
    
    if request.method == 'POST': 
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()

    context = {
        'items': items,
        'form': form,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'products_count' : products_count,
        
    }
    return render(request, 'dashboard/product.html', context)

@login_required(login_url='user-login')
def product_delete(request, pk):
    item = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    context = {'item': item}
    return render(request, 'dashboard/product_delete.html', context)

@login_required(login_url='user-login')
def product_update(request, pk):
    item = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    
    context = {
        'form': form,
        'item': item
    }
    return render(request, 'dashboard/product_update.html', context)

@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    workers_count = User.objects.all().count
    products_count = Product.objects.all().count
    
    context = {
        'orders' : orders,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'products_count' : products_count,
    }
    return render(request, 'dashboard/order.html',context)
