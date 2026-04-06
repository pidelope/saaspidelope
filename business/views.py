from django.shortcuts import render, get_object_or_404
from .models import Business, Table
from products.models import Category

def public_menu(request, business_slug, table_number):
    business = get_object_or_404(Business, slug=business_slug)
    
    # Handle takeaway case or physical table
    if table_number.lower() == 'llevar':
        table = None # Placeholder for takeaway
    else:
        table = get_object_or_404(Table, business=business, number=table_number)
    
    # Get any active order for this table to show current bill
    active_order = None
    if table:
        from orders.models import Order
        active_order = Order.objects.filter(
            business=business, 
            table=table, 
            status__in=['PENDING', 'CONFIRMED', 'READY']
        ).first()
    
    # Get categories and products
    categories = Category.objects.filter(business=business).prefetch_related('products')
    
    context = {
        'business': business,
        'table': table,
        'categories': categories,
        'active_order': active_order,
    }
    return render(request, 'business/public_menu.html', context)
