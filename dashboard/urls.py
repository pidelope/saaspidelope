from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Business selection / Multi-business
    path('', views.business_selector, name='home'),
    path('business/add/', views.business_add, name='business_add'),
    
    # Specific Business Dashboard
    path('<slug:business_slug>/', views.dashboard_home, name='business_home'),
    path('<slug:business_slug>/edit/', views.business_edit, name='business_edit'),

    # Categories
    path('<slug:business_slug>/categories/', views.category_list, name='category_list'),
    path('<slug:business_slug>/categories/add/', views.category_add, name='category_add'),
    path('<slug:business_slug>/categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('<slug:business_slug>/categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    
    # Products
    path('<slug:business_slug>/products/', views.product_list, name='product_list'),
    path('<slug:business_slug>/products/add/', views.product_add, name='product_add'),
    path('<slug:business_slug>/products/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('<slug:business_slug>/products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('<slug:business_slug>/products/<int:pk>/toggle-stock/', views.product_toggle_stock, name='product_toggle_stock'),
    
    # Staff
    path('<slug:business_slug>/staff/', views.staff_list, name='staff_list'),
    path('<slug:business_slug>/staff/add/', views.staff_add, name='staff_add'),

    # Tables & QR
    path('<slug:business_slug>/tables/', views.table_list, name='table_list'),
    path('<slug:business_slug>/tables/generate-qr/', views.generate_all_qr, name='generate_all_qr'),

    # Waiter Monitor
    path('<slug:business_slug>/monitor/', views.waiter_dashboard, name='waiter_dashboard'),
    path('<slug:business_slug>/monitor/update/<str:order_code>/<str:new_status>/', views.update_order_status, name='update_order_status'),


    # Caja
    path('<slug:business_slug>/caja/', views.caja_dashboard, name='caja_dashboard'),
]
