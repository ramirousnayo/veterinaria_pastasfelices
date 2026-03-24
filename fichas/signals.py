from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Dueno


@receiver(post_save, sender=Dueno)
def dueno_guardado(sender, instance, created, **kwargs):
    if created:
        print(f'✅ Nuevo dueño creado: {instance.nombre} ({instance.rut})')
    else:
        print(f'✏️ Dueño actualizado: {instance.nombre} ({instance.rut})')
