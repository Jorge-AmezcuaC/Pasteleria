from django.contrib import admin
from .models import (
    Empleado,
    Direccion,
    Local, 
    Compra,
    Pasteles,
    Puesto,
    Sabores,
    Ventas,
    Proveedor
)

from .adminForms import (
    PastelAdmin,
    CompraAdmin,
    DireccionAdmin,
    LocalAdmin,
    ProveedorAdmin,
    VentaAdmin,
    EmpleadoAdmin
)

admin.site.site_header = 'Mi Pasteleria'
admin.site.site_title = 'Pasteleria'
admin.site.name = "Administracion de la pasteleria"

admin.site.register(Compra, CompraAdmin)
admin.site.register(Ventas, VentaAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Local, LocalAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Direccion, DireccionAdmin)
admin.site.register(Pasteles, PastelAdmin)
admin.site.register(Sabores)
admin.site.register(Puesto)
