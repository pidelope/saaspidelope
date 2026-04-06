from django.db import models
from business.models import Business, Table
from products.models import Product
import random
import string

def generate_order_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

class Order(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pendiente'),
        ('CONFIRMED', 'Confirmado'),
        ('READY', 'Listo para entregar'),
        ('PAID', 'Pagado/Cerrado'),
        ('CANCELLED', 'Cancelado'),
    )
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='orders')
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, related_name='orders_on_table', null=True, blank=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True) # for takeaway
    code = models.CharField(max_length=6, unique=True, default=generate_order_code)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    session_token = models.CharField(max_length=100, blank=True, null=True, help_text="Tokens de la mesa para agrupar tickets de una visita.")
    client_id = models.CharField(max_length=100, blank=True, null=True, help_text="ID del dispositivo para cuentas separadas.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_total(self):
        total = sum(item.subtotal for item in self.items.all())
        self.total_amount = total
        self.save()
        return total

    def __str__(self):
        dest = f"Mesa {self.table.number}" if self.table else f"Llevar: {self.customer_name}"
        return f"{self.code} - {dest} - {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price_at_order = models.DecimalField(max_digits=10, decimal_places=2) # Snapshot of price
    notes = models.CharField(max_length=255, blank=True)

    @property
    def subtotal(self):
        return self.price_at_order * self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.product.name} ({self.order.code})"
