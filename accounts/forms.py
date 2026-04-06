from django import forms
from .models import User
from business.models import Business

class BusinessRegistrationForm(forms.ModelForm):
    # User fields
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    
    # Business fields
    business_name = forms.CharField(max_length=100)
    logo = forms.ImageField(required=False)
    slogan = forms.CharField(max_length=255, required=False)
    address = forms.CharField(max_length=255, required=False)
    phone = forms.CharField(max_length=20, required=False)

    class Meta:
        model = Business
        fields = ['name', 'logo', 'slogan', 'address', 'phone']

    def save(self):
        # Create user
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            role='ADMIN'
        )
        
        # Create business
        business = Business.objects.create(
            owner=user,
            name=self.cleaned_data['business_name'],
            logo=self.cleaned_data['logo'],
            slogan=self.cleaned_data['slogan']
        )
        return user

class StaffCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'role', 'password']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
