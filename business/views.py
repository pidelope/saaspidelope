from django.shortcuts import render, get_object_or_404
from .models import Business, Table
from products.models import Category

def public_menu(request, business_slug, table_number):
    business = get_object_or_404(Business, slug=business_slug)
    # The table_number is just for tracking who makes the order
    table = get_object_or_404(Table, business=business, number=table_number)
    
    # Get categories and products
    categories = Category.objects.filter(business=business).prefetch_related('products')
    
    context = {
        'business': business,
        'table': table,
        'categories': categories,
    }
    return render(request, 'business/public_menu.html', context)
