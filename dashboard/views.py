from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import CategoryForm, ProductForm, StaffRegistrationForm
from products.models import Category, Product
from accounts.models import User
from business.models import Business, Table
from django import forms

# --- Forms Enhancement ---
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'logo', 'slogan', 'address', 'phone', 'menu_background', 'menu_text_color']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-input'}),
            'slogan': forms.TextInput(attrs={'class': 'form-input'}),
            'address': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
            'menu_background': forms.ClearableFileInput(attrs={'class': 'form-input'}),
            'menu_text_color': forms.TextInput(attrs={'class': 'form-input', 'type': 'color'}),
        }

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['number', 'is_active']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. 01, VIP-01, Barra'}),
        }

# --- Decorators & Helpers ---
def admin_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role != 'ADMIN':
            return HttpResponse("No tienes permisos.", status=403)
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def get_business(user, slug):
    return get_object_or_404(Business, owner=user, slug=slug)

# --- Views ---
@admin_required
def business_selector(request):
    businesses = request.user.businesses.all()
    if businesses.count() == 1:
        return redirect('dashboard:business_home', business_slug=businesses.first().slug)
    return render(request, 'dashboard/business_selector.html', {'businesses': businesses})

@admin_required
def business_add(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.owner = request.user
            business.save()
            return redirect('dashboard:business_home', business_slug=business.slug)
    else:
        form = BusinessForm()
    return render(request, 'dashboard/business_form.html', {'form': form})

@admin_required
def business_edit(request, business_slug):
    business = get_business(request.user, business_slug)
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES, instance=business)
        if form.is_valid():
            form.save()
            return redirect('dashboard:business_home', business_slug=business.slug)
    else:
        form = BusinessForm(instance=business)
    return render(request, 'dashboard/business_form.html', {'form': form, 'business': business})

@admin_required
def dashboard_home(request, business_slug):
    business = get_business(request.user, business_slug)
    context = {
        'business': business,
        'categories_count': business.categories.count(),
        'products_count': Product.objects.filter(category__business=business).count(),
        'staff_count': business.staff.count(),
        'active_orders': business.orders.exclude(status='PAID').count()
    }
    return render(request, 'dashboard/home.html', context)

# --- Categories ---
@admin_required
def category_list(request, business_slug):
    business = get_business(request.user, business_slug)
    categories = business.categories.all()
    return render(request, 'dashboard/categories/list.html', {'categories': categories, 'business': business})

@admin_required
def category_add(request, business_slug):
    business = get_business(request.user, business_slug)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.business = business
            category.save()
            return redirect('dashboard:category_list', business_slug=business.slug)
    else:
        form = CategoryForm()
    return render(request, 'dashboard/categories/form.html', {'form': form, 'business': business})

@admin_required
def category_edit(request, business_slug, pk):
    business = get_business(request.user, business_slug)
    category = get_object_or_404(Category, pk=pk, business=business)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('dashboard:category_list', business_slug=business.slug)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'dashboard/categories/form.html', {'form': form, 'business': business})

@admin_required
def category_delete(request, business_slug, pk):
    business = get_business(request.user, business_slug)
    category = get_object_or_404(Category, pk=pk, business=business)
    if request.method == 'POST':
        category.delete()
        return redirect('dashboard:category_list', business_slug=business.slug)
    return render(request, 'dashboard/confirm_delete.html', {'object': category, 'type': 'Categoría', 'business': business})

# --- Products ---
@admin_required
def product_list(request, business_slug):
    business = get_business(request.user, business_slug)
    products = Product.objects.filter(category__business=business)
    return render(request, 'dashboard/products/list.html', {'products': products, 'business': business})

@admin_required
def product_add(request, business_slug):
    business = get_business(request.user, business_slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, business=business)
        if form.is_valid():
            form.save()
            return redirect('dashboard:product_list', business_slug=business.slug)
    else:
        form = ProductForm(business=business)
    return render(request, 'dashboard/products/form.html', {'form': form, 'business': business})

@admin_required
def product_edit(request, business_slug, pk):
    business = get_business(request.user, business_slug)
    product = get_object_or_404(Product, pk=pk, category__business=business)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product, business=business)
        if form.is_valid():
            form.save()
            return redirect('dashboard:product_list', business_slug=business.slug)
    else:
        form = ProductForm(instance=product, business=business)
    return render(request, 'dashboard/products/form.html', {'form': form, 'business': business})

@admin_required
def product_toggle_stock(request, business_slug, pk):
    business = get_business(request.user, business_slug)
    product = get_object_or_404(Product, pk=pk, category__business=business)
    product.is_available = not product.is_available
    product.save()
    label = "✅ Disponible" if product.is_available else "❌ Agotado"
    color = "#2e7d32" if product.is_available else "#c62828"
    
    # Retornamos el mismo elemento con los atributos de HTMX para que siga siendo cliqueable
    html = f'''
    <span style="color: {color}; font-size: 0.75rem; font-weight: 700; cursor: pointer;" 
          hx-post="/dashboard/{business_slug}/products/toggle-stock/{pk}/" 
          hx-target="#stock-{pk}" hx-swap="innerHTML">{label}</span>
    '''
    return HttpResponse(html)

@admin_required
def product_delete(request, business_slug, pk):
    business = get_business(request.user, business_slug)
    product = get_object_or_404(Product, pk=pk, category__business=business)
    if request.method == 'POST':
        product.delete()
        return redirect('dashboard:product_list', business_slug=business.slug)
    return render(request, 'dashboard/confirm_delete.html', {'object': product, 'type': 'Producto', 'business': business})

# --- Staff ---
@admin_required
def staff_list(request, business_slug):
    business = get_business(request.user, business_slug)
    staff = business.staff.all()
    return render(request, 'dashboard/staff/list.html', {'staff': staff, 'business': business})

@admin_required
def staff_add(request, business_slug):
    business = get_business(request.user, business_slug)
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.assigned_business = business
            user.save()
            return redirect('dashboard:staff_list', business_slug=business.slug)
    else:
        form = StaffRegistrationForm()
    return render(request, 'dashboard/staff/form.html', {'form': form, 'business': business})

# --- Tables & QR ---
@admin_required
def table_list(request, business_slug):
    business = get_business(request.user, business_slug)
    tables = business.tables.all()
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            table = form.save(commit=False)
            table.business = business
            table.save()
            return redirect('dashboard:table_list', business_slug=business.slug)
    else:
        form = TableForm()
    return render(request, 'dashboard/tables/list.html', {'tables': tables, 'form': form, 'business': business})

@admin_required
def generate_all_qr(request, business_slug):
    business = get_business(request.user, business_slug)
    return render(request, 'dashboard/tables/qr_printable.html', {'business': business})

# --- Waiter / Order Monitor ---
@login_required
def waiter_dashboard(request, business_slug):
    # This view is for WAITERS or ADMINS
    business = get_object_or_404(Business, slug=business_slug)
    if request.user.role not in ['ADMIN', 'WAITER']:
        return HttpResponse("Acceso denegado.", status=403)
    
    orders = business.orders.exclude(status__in=['PAID', 'CANCELLED']).order_by('-created_at')
    
    return render(request, 'dashboard/waiter/monitor.html', {
        'business': business,
        'orders': orders,
        # Group by column
        'pending': orders.filter(status='PENDING'),
        'confirmed': orders.filter(status='CONFIRMED'),
        'ready': orders.filter(status='READY'),
    })

@login_required
def update_order_status(request, business_slug, order_code, new_status):
    business = get_object_or_404(Business, slug=business_slug)
    from orders.models import Order
    order = get_object_or_404(Order, code=order_code, business=business)
    
    if new_status in [s[0] for s in Order.STATUS_CHOICES]:
        order.status = new_status
        order.save()
    
    # Redirect to where the request came from
    referer = request.META.get('HTTP_REFERER')
    if referer and 'caja' in referer:
        return redirect('dashboard:caja_dashboard', business_slug=business.slug)
    return redirect('dashboard:waiter_dashboard', business_slug=business.slug)

# --- Staff Management ---
@admin_required
def staff_list(request, business_slug):
    business = get_business(request.user, business_slug)
    staff = business.staff.all()
    return render(request, 'dashboard/staff/list.html', {'business': business, 'staff': staff})

@admin_required
def staff_add(request, business_slug):
    business = get_business(request.user, business_slug)
    from accounts.forms import StaffCreationForm # We need to create this
    if request.method == 'POST':
        form = StaffCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.assigned_business = business
            user.save()
            return redirect('dashboard:staff_list', business_slug=business.slug)
    else:
        form = StaffCreationForm()
    return render(request, 'dashboard/staff/form.html', {'business': business, 'form': form})

# --- Caja / Checkout ---
@login_required
def caja_dashboard(request, business_slug):
    # For ADMIN or CASHIER
    business = get_object_or_404(Business, slug=business_slug)
    if request.user.role not in ['ADMIN', 'CASHIER']:
        return HttpResponse("Acceso denegado.", status=403)
    
    from django.utils import timezone
    today = timezone.now().date()
    
    # Orders to pay (READY)
    to_pay = business.orders.filter(status='READY')
    
    # Daily Sales (PAID today)
    paid_today = business.orders.filter(status='PAID', updated_at__date=today)
    total_revenue = sum(o.total_amount for o in paid_today)
    
    return render(request, 'dashboard/caja/monitor.html', {
        'business': business,
        'to_pay': to_pay,
        'paid_today': paid_today,
        'total_revenue': total_revenue
    })
