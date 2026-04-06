import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from business.models import Business, Table
from products.models import Product
from .models import Order, OrderItem

@csrf_exempt # In a real app we'd use the CSRF token properly, but for this demo/local test:
def submit_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            business_id = data.get('business_id')
            table_id = data.get('table_id')
            customer_name = data.get('customer_name')
            cart_items = data.get('items', [])
            
            business = get_object_or_404(Business, id=business_id)
            
            table = None
            if table_id:
                table = get_object_or_404(Table, id=table_id, business=business)
            
            # Create Order
            order = Order.objects.create(
                business=business,
                table=table,
                customer_name=customer_name,
                status='PENDING'
            )
            
            total = 0
            for item in cart_items:
                product = get_object_or_404(Product, id=item['id'])
                qty = item['qty']
                price = product.price
                
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=qty,
                    price_at_order=price
                )
                total += (price * qty)
            
            order.total_amount = total
            order.save()
            
            return JsonResponse({
                'status': 'success',
                'order_code': order.code,
                'message': '¡Pedido enviado con éxito!'
            })
            
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Solo peticiones POST'}, status=405)
