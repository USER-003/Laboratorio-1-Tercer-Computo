from django.db import models

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    edad = models.IntegerField()
    dui = models.IntegerField()

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_del_area = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    edad = models.IntegerField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_venta = models.DateTimeField()
    monto = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
