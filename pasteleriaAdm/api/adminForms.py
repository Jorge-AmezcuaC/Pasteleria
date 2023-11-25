from django.contrib import admin
from .models import CompraProductos, Sabores, VentaPasteles, Puesto

class CompraProductoInLine(admin.TabularInline):
    autocomplete_fields = ('pastel',)
    model = CompraProductos
    extra = 1

class VentaProductoInLine(admin.TabularInline):
    autocomplete_fields = ('pastel',)
    readonly_fields = ('subtotal',)
    model = VentaPasteles
    extra = 1

class CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'proveedor', 'total')
    search_fields = ('id', 'fecha', 'proveedor__nombre')
    # autocomplete_fields = ('proveedor', )
    inlines = [CompraProductoInLine]
    readonly_fields = ('total', 'fecha')
    date_hierarchy = ('fecha')

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'empleado', 'total')
    search_fields = ('id', 'fecha', 'empleado')
    # autocomplete_fields = ('proveedor', )
    inlines = [VentaProductoInLine]
    readonly_fields = ('total', 'fecha')
    date_hierarchy = ('fecha')

class PastelAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sabor', 'stock', 'tamano', 'precio')
    search_fields = ('nombre', 'sabor__sabor',)
    readonly_fields = ('stock',)
    # autocomplete_fields = ('sabor',)

class DireccionAdmin(admin.ModelAdmin):
    list_display = ('cp', 'estado', 'municipio', 'colonia', 'calle', 'numeroInt', 'numeroExt')
    search_fields = ('cp', 'estado', 'municipio', 'calle')

class LocalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'Telefono', 'direccion')
    search_fields = ('nombre', 'Telefono')
    autocomplete_fields = ('direccion',)

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre',  'correo', 'telefono',)
    search_fields = ('nombre',  'correo', 'telefono',)
    
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('rfc', 'nombre', 'telefono', 'cargo', 'local', 'sueldo')
    search_fields = ('rfc', 'nombre', )
    exclude = ('last_login', 'is_superuser', 'groups', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'user_permissions')