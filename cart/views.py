# from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,redirect, get_object_or_404
from .models import QuotationInfo,QuotationItem
from item.models import Item
from .forms import quotationForm

def view_cart(request):
    cart_items=request.session.get('cart_items',[])
    return render(request, 'cart/cart.html', {
        'cart_items':cart_items,
    })

def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    specification = request.POST.get('specification','')
    quantity=request.POST.get('quantity', '')

    cart_items = request.session.get('cart_items', [])

    cart_items.append({
        'item_id': item.id,
        'item_name': item.name,
        'specification': specification,
        'quantity': quantity
    })
    request.session['cart_items'] = cart_items

    return redirect('cart:view_cart')

def remove_from_cart(request, item_id):
    cart_item = request.session.get('cart_item',[])
    cart_items = [item for item in cart_items if item['item_id'] != item_id]
    request.session['cart_items'] = cart_items
    
    return redirect('cart:view_cart')

def submit_quotation(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        cart_items = request.session.get('cart_items', [])

        if cart_items:
            # 創建 QuotationInfo 物件
            quotation = QuotationInfo.objects.create(username=username, email=email)

            for item in cart_items:
                item_obj = get_object_or_404(Item, id=item['item_id'])
                QuotationItem.objects.create(
                    quotation=quotation,
                    item=item_obj,
                    specification=item['specification'],
                    quantity=item['quantity']
                )
            request.session['cart_items'] = []

            return redirect('cart:view_cart')
        return redirect('cart:view_cart')