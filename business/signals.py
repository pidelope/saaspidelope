from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Business
import cloudinary.uploader

@receiver(post_delete, sender=Business)
def delete_business_images(sender, instance, **kwargs):
    """Borra las imágenes cuando se elimina un Business."""
    if instance.logo:
        instance.logo.delete(save=False)
    if instance.menu_background:
        instance.menu_background.delete(save=False)

@receiver(pre_save, sender=Business)
def delete_old_business_images(sender, instance, **kwargs):
    """Borra las imágenes antiguas de Cloudinary cuando se actualizan."""
    if not instance.pk:
        return False

    try:
        old_instance = Business.objects.get(pk=instance.pk)
    except Business.DoesNotExist:
        return False

    # Verificar Logo
    if old_instance.logo and old_instance.logo != instance.logo:
        old_instance.logo.delete(save=False)

    # Verificar Fondo de Menú
    if old_instance.menu_background and old_instance.menu_background != instance.menu_background:
        old_instance.menu_background.delete(save=False)
