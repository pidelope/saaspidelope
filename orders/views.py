import json
from django.shortcuts import render, get_object_or_404
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
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
            session_token = data.get('session_token')
            client_id = data.get('client_id')
            cart_items = data.get('items', [])
            
            business = get_object_or_404(Business, id=business_id)
            
            table = None
            if table_id:
                table = get_object_or_404(Table, id=table_id, business=business)
                
                # Security Check: Compare session tokens
                if str(table.session_token) != str(session_token):
                    return JsonResponse({
                        'status': 'error', 
                        'message': 'Esta sesión ha expirado o ya se realizó el pago. Por favor, escanea el código QR nuevamente.'
                    }, status=403)
            
            # Individual Order Scope: Same table AND same client device
            order = None
            if table and client_id:
                order = Order.objects.filter(
                    business=business, 
                    table=table,
                    client_id=client_id,
                    status__in=['PENDING', 'CONFIRMED', 'READY']
                ).first()
            
            if not order:
                # Security Check: Table must be open to start a NEW order
                if table and not table.is_open:
                    return JsonResponse({
                        'status': 'error', 
                        'message': 'Esta mesa está cerrada. Por favor solicita al personal que la abra para realizar un nuevo pedido.'
                    }, status=403)
                
                # Create a NEW Order for this specific client
                order = Order.objects.create(
                    business=business,
                    table=table,
                    customer_name=customer_name,
                    session_token=session_token,
                    client_id=client_id,
                    status='PENDING'
                )
            
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
            
            # Recalculate total
            order.calculate_total()
            
            # Signal WebSockets
            try:
                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    f"orders_{business.slug}",
                    {
                        "type": "order_update",
                    }
                )
            except Exception as e:
                print(f"WS Signal Error: {e}")

            return JsonResponse({
                'status': 'success',
                'order_code': order.code,
                'total_amount': float(order.total_amount),
                'message': '¡Pedido enviado con éxito!'
            })
            
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Solo peticiones POST'}, status=405)
