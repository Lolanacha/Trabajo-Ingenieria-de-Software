from django.db import models
# aqui se crean los modelos de la base de datos
# a través de clases que heredan de models.Model

class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    comuna = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    numero_de_casa = models.IntegerField()
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Producto(models.Model):
    SKU = models.CharField(primary_key=True, max_length=50, unique=True)
    tipo_producto = models.CharField(max_length=50)
    viña= models.CharField(max_length=150)
    cepa= models.CharField(max_length=50)
    nombre_producto = models.CharField(max_length=50)
    cosecha = models.CharField(max_length=50)
    def __str__(self):
        return self.SKU  

class Ventas(models.Model):
    SKU = models.ForeignKey(Producto, on_delete=models.CASCADE, default='1')
    numero_boleta = models.IntegerField(unique=True)
    nombre_producto = models.CharField(max_length=50)
    precio_unitario = models.IntegerField()
    cantidad = models.IntegerField()
    iva = models.IntegerField()
    medio_de_pago = models.CharField(max_length=50)

    def str(self):
        return f"{self.SKU.SKU} - {self.nombre_producto}"

    

class Inventario_Y_Stock(models.Model):
    id_inventario=models.CharField(primary_key=True, max_length=50, unique=True, default='0')
    SKU = models.CharField(max_length=50, unique=True)
    nombre_producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()
    fecha_de_ingreso = models.DateTimeField()
    Venta = models.BooleanField(default=False)
  
      
class Proveedores(models.Model):
    rut_empresa = models.CharField(primary_key=True, max_length=12, unique=True) # primary key
    nombre_prov = models.CharField(max_length=50)
    email_empresa = models.EmailField()
    telefono_empresa = models.IntegerField()
    #SKU_prov = models.ForeignKey(Compra_proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_prov + ' ' + self.rut_empresa
    
class Compra_proveedores(models.Model):
    Numero_casa = models.IntegerField()
    Calle_casa = models.CharField(max_length=255)
    producto = models.CharField(max_length=50)
    numero = models.IntegerField()
    SKU_prov = models.CharField(max_length=50) # foreign key para compra de proveedor
    #SKU_prov = models.ForeignKey(Compra_proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.producto + ' ' + self.numero

class Informes(models.Model):
    fecha_informe =models.DateField()
    cantidad_ventas = models.IntegerField()
    transacciones = models.IntegerField()
    cantidad_miembros = models.IntegerField()
    ingresos_ventas = models.IntegerField()
    gastos_ventas = models.IntegerField()
    gastos_no_ventas = models.IntegerField()
    def __str__(self):
        return self.fecha_informe

class Alerta_stock(models.Model):
    id_inventario=models.ForeignKey(Inventario_Y_Stock, on_delete=models.CASCADE, default='0')
    fecha_alerta = models.DateField()
      # Corregido: No necesitas una relación ForeignKey aquí

    def __str__(self):
        return str(self.id_inventario) + ' ' + str(self.fecha_alerta)
    
"""class Alerta_informes(models.Model):
    # Cambiado el related_name a 'alertas_informes'
    ventas = models.ForeignKey(Ventas, on_delete=models.CASCADE, related_name='alertas_informes')
    fecha_alerta = models.DateField()

    def __str__(self):
        return str(self.ventas.numero_boleta) + ' ' + str(self.fecha_alerta)"""
    

