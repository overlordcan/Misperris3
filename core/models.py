from django.db import models

# Create your models here.


class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

class Region(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"

class Vivienda(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Postulante(models.Model): 
    correo = models.EmailField(max_length=254)
    run = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=254)
    fecha_nacimiento=models.DateField(auto_now=False, auto_now_add=False)
    telefono = models.IntegerField()
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)

    def __str__(self):
        return self.run
    class Meta:
        verbose_name = "Postulante"
        verbose_name_plural = "Postulantes"


class Raza(models.Model):
    nombre = models.CharField(max_length=50)
    

    def __str__(self):
        return self.nombre



class Estado(models.Model):
    nombre = models.CharField(max_length=50)
    

    def __str__(self):
        return self.nombre
    

class Mascotas(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    fecha_ingreso = models.CharField(max_length=50)
    fecha_nacimiento = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)   
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    #imagen = models.ImageField(blank=True)

    def __str__(self):
        return self.nombre

    class meta:
        verbose_name ="Mascota"
        verbose_name_plutal="Mascotas"

