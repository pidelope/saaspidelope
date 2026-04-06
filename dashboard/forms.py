from django import forms
from products.models import Category, Product
from accounts.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'is_quick_service']
        labels = {
            'is_quick_service': '⚡ Servicio Rápido (Bebidas, bar, etc.)',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Ceviches, Bebidas...'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 2, 'placeholder': 'Descripción opcional (Ej: Lo mejor del mar)'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'is_available']
        labels = {
            'name': 'Nombre del plato',
            'category': 'Categoría',
            'description': 'Reseña / Ingredientes',
            'price': 'Precio',
            'is_available': 'En Stock / Disponible',
        }
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Ceviche Clásico'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Descripción detallada'}),
            'price': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.10'}),
        }

    def __init__(self, *args, **kwargs):
        business = kwargs.pop('business', None)
        super().__init__(*args, **kwargs)
        if business:
            self.fields['category'].queryset = Category.objects.filter(business=business)

class StaffRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'phone']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].choices = [
            ('WAITER', 'Mesero'),
            ('CASHIER', 'Cajero'),
        ]
