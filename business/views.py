from django.shortcuts import render, get_object_or_404
from .models import Business, Table
from products.models import Category

def public_menu(request, business_slug, table_number):
    import uuid
    business = get_object_or_404(Business, slug=business_slug)
    
    # Handle Individual Client Identity via Cookie
    client_id = request.COOKIES.get('pideya_client_id')
    new_client = False
    if not client_id:
        client_id = str(uuid.uuid4())
        new_client = True
    
    # Handle takeaway case or physical table
    if table_number.lower() == 'llevar':
        table = None # Placeholder for takeaway
    else:
        table = get_object_or_404(Table, business=business, number=table_number)
    
    # Get active order ONLY for this specific client device
    active_order = None
    if table:
        from orders.models import Order
        active_order = Order.objects.filter(
            business=business, 
            table=table,
            client_id=client_id, # Filter by Device
            status__in=['PENDING', 'CONFIRMED', 'READY', 'PAID'] # Show even if paid for summary
        ).exclude(status='CANCELLED').order_by('-created_at').first()
    
    # Get categories and products
    categories = Category.objects.filter(business=business).prefetch_related('products')
    
    context = {
        'business': business,
        'table': table,
        'categories': categories,
        'active_order': active_order,
        'session_token': table.session_token if table else None,
        'client_id': client_id,
    }
    
    response = render(request, 'business/public_menu.html', context)
    if new_client:
        # Set persistent cookie for 30 days
        response.set_cookie('pideya_client_id', client_id, max_age=86400 * 30, httponly=True)
    return response
