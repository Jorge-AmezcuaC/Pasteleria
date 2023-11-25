from django.contrib import admin
from .models import (
    Empleado,
    Direccion,
    Estado,
    Local, 
    Municipio,
    Pasteles,
    Puesto,
    Sabores,
    VentaPasteles,
    Ventas
)

admin.site.register(Empleado)
admin.site.register(Direccion)
admin.site.register(Estado)
admin.site.register(Local)
admin.site.register(Municipio)
admin.site.register(Pasteles)
admin.site.register(Puesto)
admin.site.register(Sabores)
admin.site.register(VentaPasteles)
admin.site.register(Ventas)
