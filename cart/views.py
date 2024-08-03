from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,redirect, get_object_or_404
from .models import CartItem
from item.models import Item
from .forms import quotationForm

def view_cart(request):
    cart_items=CartItem.objects.all()
    return render(request, 'cart/cart.html', {
        'cart_items':cart_items,
    })

def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == "POST":
        specification = request.POST.get('specification')
        cart_item, created = CartItem.objects.get_or_create(item=item, specification=specification)
        if not created:
            cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:view_cart')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')

def submit_quotation(request):
    if request.method == "POST":
        form = quotationForm(request.POST)
        if form.is_valid():
            specification = form.cleaned_data['specification']
            cart_items = CartItem.objects.filter(user=request.user)
            cart_items.delete()
            return redirect('cart:view_cart')
        else:
            return quotationForm()
    return render(request, 'cart/cart.html', {'form': form})