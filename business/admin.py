from django.contrib import admin
from .models import Business, Table

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'owner', 'is_active', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug')

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'business', 'is_active')
    list_filter = ('business', 'is_active')
