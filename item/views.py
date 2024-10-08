from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Item, Category
from cart.forms import quotationForm

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.all()
    
    if category_id:
        category_id = int(category_id)
        items = items.filter(category_id=category_id)
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    paginate_by = 16
    paginator = Paginator(items, paginate_by)
    page = request.GET.get('page')
    
    try:
        items_paginated = paginator.page(page)
    except PageNotAnInteger:
        items_paginated = paginator.page(1)
    except EmptyPage:
        items_paginated = paginator.page(paginator.num_pages)

    context = {
        'query': query,
        'category_id': category_id,
        'categories': categories,
        'items': items_paginated,
        'page_obj': items_paginated,
    }
    
    return render(request, 'item/items.html', context)

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item.category == '避震器':
        related_items = Item.objects.filter(name__icontains='防震接頭')
    else:
        related_items = Item.objects.filter(category=item.category).exclude(pk=pk)[:3]
    
    if request.method == "POST":
        form = quotationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=pk)
    else:
        form = quotationForm()

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
        'form': form,
    })
