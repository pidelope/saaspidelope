from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Product
import cloudinary.uploader

@receiver(post_delete, sender=Product)
def delete_product_image(sender, instance, **kwargs):
    """Borra la imagen cuando se elimina un Producto."""
    if instance.image:
        instance.image.delete(save=False)

@receiver(pre_save, sender=Product)
def delete_old_product_image(sender, instance, **kwargs):
    """Borra la imagen antigua de Cloudinary cuando se actualiza el producto."""
    if not instance.pk:
        return False

    try:
        old_instance = Product.objects.get(pk=instance.pk)
    except Product.DoesNotExist:
        return False

    if old_instance.image and old_instance.image != instance.image:
        old_instance.image.delete(save=False)
