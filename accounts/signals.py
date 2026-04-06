from allauth.socialaccount.signals import social_account_added
from django.dispatch import receiver
from business.models import Business


@receiver(social_account_added)
def create_business_on_google_signup(sender, request, sociallogin, **kwargs):
    """
    Cuando un socio se registra por primera vez con Google,
    se crea automáticamente un negocio con email como nombre provisional.
    El socio puede renombrarlo y crear más negocios/sedes después.
    """
    user = sociallogin.user

    # Solo si no tiene ningún negocio creado aún
    if not Business.objects.filter(owner=user).exists():
        provisional_name = user.email  # Ej: "juan@gmail.com"
        Business.objects.create(
            owner=user,
            name=provisional_name,
        )

    # Asegurar que el rol sea ADMIN
    if user.role != 'ADMIN':
        user.role = 'ADMIN'
        user.save(update_fields=['role'])
