from django.contrib import admin
from .models import Category, Product, OptionGroup, ProductOption

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'business', 'is_quick_service')
    list_filter = ('business', 'parent', 'is_quick_service')
    search_fields = ('name', 'description')

class OptionGroupInline(admin.TabularInline):
    model = OptionGroup
    extra = 1
    show_change_link = True

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available')
    list_filter = ('category', 'category__business', 'is_available')
    search_fields = ('name', 'description')
    inlines = [OptionGroupInline]

class ProductOptionInline(admin.TabularInline):
    model = ProductOption
    extra = 2

@admin.register(OptionGroup)
class OptionGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'min_selectable', 'max_selectable')
    list_filter = ('product__category__business', 'product')
    search_fields = ('name', 'product__name')
    inlines = [ProductOptionInline]

@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'price_modifier', 'is_available')
    list_filter = ('group__product__category__business', 'is_available')
    search_fields = ('name', 'group__name', 'group__product__name')
