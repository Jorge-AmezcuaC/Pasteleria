from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser  

class Sabores(models.Model):
    sabor = models.CharField(max_length=25, primary_key=True)

    def __str__(self):
        return f"{self.sabor}"
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=25, primary_key=True)
    telefono = models.CharField(max_length=12)
    correo = models.EmailField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nombre}"

class Puesto(models.Model):
    puesto = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return f"{self.puesto}"

class Pasteles(models.Model):
    nombre = models.CharField(max_length=30)
    receta = models.CharField(max_length=255)
    precio = models.FloatField()
    stock = models.IntegerField()
    tamano = models.IntegerField()
    sabor = models.ForeignKey(Sabores, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.sabor} {self.tamano}cm {self.stock} ${self.precio}"

class Direccion(models.Model):
    colonia = models.CharField(max_length=50)
    calle = models.CharField(max_length=75)
    cp = models.CharField(max_length=5)
    numeroInt = models.CharField(max_length=15)
    numeroExt = models.CharField(max_length=15)
    estado = models.CharField(max_length=25)
    municipio = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.cp} {self.estado} {self.municipio} {self.colonia} {self.calle}"

class Local(models.Model):
    nombre = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=12)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.Telefono}"

class Empleado(AbstractUser):
    rfc = models.CharField(max_length=18, unique=True)
    nombre = models.CharField(max_length=50)
    sueldo = models.FloatField(null=True)
    telefono = models.CharField(max_length=12, null=True)
    cargo = models.ForeignKey(Puesto, on_delete=models.CASCADE, null=True)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.rfc} {self.nombre} {self.cargo} {self.local}"

class Ventas(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    total = models.FloatField(default=0)

    def __str__(self):
        return f"{self.fecha} {self.empleado} {self.total}"
    
class VentaPasteles(models.Model):
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    pastel = models.ForeignKey(Pasteles, on_delete=models.CASCADE)
    unidades = models.IntegerField()
    subtotal = models.FloatField(default=0)

    def __str__(self):
        return f"{self.venta} {self.unidades} {self.pastel} {self.subtotal}"
    
    def save(self, *args, **kwargs):
        self.subtotal = self.unidades * self.pastel.precio

        super(VentaPasteles, self).save(*args, **kwargs)
    
class Compra(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    total = models.FloatField(default=0)

    def __str__(self):
        return f"{self.fecha} {self.proveedor} {self.total}"
    
class CompraProductos(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    pastel = models.ForeignKey(Pasteles, on_delete=models.CASCADE)
    unidades = models.IntegerField()
    subtotal = models.FloatField(default=0)

    def __str__(self):
        return f"{self.compra} {self.unidades} {self.pastel} {self.subtotal}"