from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from .models import Item, Category
from item.forms import QuotationForm
from django.core.mail import send_mail
from django.conf import settings

def add_item_to_quotation(request,pk):
    item=get_object_or_404(Item,pk=pk)
    if request.method=="POST":
        form=QuotationForm(request.POST)
        if form.is_valid():
            quotation_cart=request.session.get('quotation_cart',[])
            quotation_cart.append({
                'item_id':item.id,
                'specification': form.cleaned_data['specification'],
                'quantity': form.cleaned_data['quantity'],
                'name': item.name,
            })
            request.session['quotation_cart'] = quotation_cart
            return redirect('quotation_summary')
        else:
            form=QuotationForm()
        return render(request, 'item/add_to_quotation.html',{
            'form':form,
            'item':item,
        })
def quotation_summary(request):
    quotation_cart = request.session.get('quotation_cart', [])
    return render(request, 'item/quotation_summary.html', {'quotation_cart': quotation_cart})
def submit_quotation(request):
    quotation_cart = request.session.get('quotation_cart', [])
    if quotation_cart:
        # 在這裡處理詢價單，例如發送電子郵件
        subject = '新的詢價請求'
        message = ''
        for item in quotation_cart:
            message += f"品項: {item['name']}, 規格: {item['specification']}, 數量: {item['quantity']}\n"
        
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['jj0985788718@gmail.com'])
        
        # 清空詢價單
        request.session['quotation_cart'] = []
        
        return render(request, 'core/quotation_submitted.html')
    return redirect('quotation_summary')

def items(request):
    query=request.GET.get('query','')
    category_id=request.GET.get('category', 0)
    categories=Category.objects.all()
    items=Item.objects.all()
    paginate_by = 16
    paginator = Paginator(items, paginate_by)
    page = request.GET.get('page')

    try:
        items_paginated = paginator.page(page)
    except PageNotAnInteger:
        # 如果 page 不是整數，返回第一頁
        items_paginated = paginator.page(1)
    except EmptyPage:
        # 如果 page 超出範圍，返回最後一頁
        items_paginated = paginator.page(paginator.num_pages)

    context = {
        'query': query,
        'category_id': category_id,
        'categories': categories,
        'items': items_paginated,
        'page_obj':items_paginated,
    }
    
    if category_id:
        items=items.filter(category_id=category_id)
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request,'item/items.html', context)


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item.category == '避震器':
        related_items = Item.objects.filter(name__icontains='防震接頭')
    else:
        related_items = Item.objects.filter(category=item.category).exclude(pk=pk)[:3]
    return render(request, 'item/detail.html',{
        'item':item,
        'related_items':related_items,
    })