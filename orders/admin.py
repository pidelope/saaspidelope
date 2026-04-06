from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('price_at_order', 'subtotal') # Subtotal handled by property, price_at_order snapshot

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('code', 'business', 'table', 'customer_name', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'business', 'created_at')
    inlines = [OrderItemInline]
    search_fields = ('code', 'customer_name')
