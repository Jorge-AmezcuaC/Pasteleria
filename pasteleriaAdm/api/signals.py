from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import VentaPasteles, CompraProductos, Ventas, Compra
from django.db.models import Sum

@receiver(post_save, sender=VentaPasteles)
def update_venta_total(sender, instance, created, **kwargs):
    if created:
        subtotals = instance.ventapasteles_set.aggregate(Sum('subtotal'))
        instance.total = subtotals['subtotal__sum'] or 0
        instance.save()