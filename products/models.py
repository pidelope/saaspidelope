from django.db import models
from business.models import Business

class Category(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='categories')
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='subcategories',
        help_text="Categoría principal de la cual depende esta subcategoría."
    )
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    is_quick_service = models.BooleanField(default=False, help_text="Marcar para bebidas/bar que el mozo puede servir rápido.")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} > {self.name}"
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.category.name}"

class OptionGroup(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='option_groups')
    name = models.CharField(max_length=100, help_text="Ej. Preparación de Huevos, Elección de Bebida, Extras")
    min_selectable = models.PositiveIntegerField(
        default=1, 
        help_text="0 para opcional (como adicionales extras), 1 para obligatorio (como término de cocción)"
    )
    max_selectable = models.PositiveIntegerField(
        default=1, 
        help_text="1 para selección única (radio), >1 para selección múltiple (checkboxes)"
    )

    def __str__(self):
        return f"{self.product.name} - {self.name}"

class ProductOption(models.Model):
    group = models.ForeignKey(OptionGroup, on_delete=models.CASCADE, related_name='options')
    name = models.CharField(max_length=100) # Ej. "Huevos Fritos", "Café Americano", "Queso"
    price_modifier = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00, 
        help_text="Costo adicional (ej. +3.00 para extras o 0.00 para incluido/gratis)"
    )
    is_available = models.BooleanField(default=True)

    def __str__(self):
        sign = "+" if self.price_modifier >= 0 else ""
        price_label = f" ({sign}S/. {self.price_modifier})" if self.price_modifier != 0 else " (Incluido)"
        return f"{self.group.name}: {self.name}{price_label}"
