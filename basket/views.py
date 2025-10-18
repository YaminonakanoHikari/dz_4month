from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Order
from .forms import CustomerForm, OrderForm

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'basket/order_list.html', {'orders': orders})

def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'basket/order_form.html', {'form': form})

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'basket/order_form.html', {'form': form})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect('order_list')
    return render(request, 'basket/order_confirm_delete.html', {'order': order})
