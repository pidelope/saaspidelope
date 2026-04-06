from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Business(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='businesses')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    slogan = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    menu_background = models.ImageField(upload_to='menu_backgrounds/', blank=True, null=True)
    menu_text_color = models.CharField(max_length=10, default='#000000')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            # Guarantee uniqueness: append pk of owner if already taken
            slug_candidate = base_slug
            counter = 1
            while Business.objects.filter(slug=slug_candidate).exclude(pk=self.pk).exists():
                slug_candidate = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug_candidate
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

import uuid

class Table(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='tables')
    number = models.CharField(max_length=10) # Can be '1', '2' or 'VIP-1'
    is_active = models.BooleanField(default=True) # If delete/disable
    is_open = models.BooleanField(default=False) # If ready for orders
    session_token = models.UUIDField(default=uuid.uuid4, null=True, blank=True)

    def rotate_session(self):
        """Generates a new token to invalidate previous customers"""
        self.session_token = uuid.uuid4()
        self.save()

    def __str__(self):
        return f"{self.business.name} - Mesa {self.number}"
