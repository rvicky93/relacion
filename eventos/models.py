from django.db import models
from django.contrib import admin
class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return self.nombre
class TipoEvento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
class Evento(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField()
    tipo = models.ForeignKey(TipoEvento, on_delete=models.CASCADE,
                            blank=True, null=True)
    personas   = models.ManyToManyField(Persona, through='Inscripcion')
    def __str__(self):
        return self.nombre
class Inscripcion(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
class InscripcionInLine(admin.TabularInline):
    model = Inscripcion
    extra = 1
class PersonaAdmin(admin.ModelAdmin):
    inlines = (InscripcionInLine,)
class EventoAdmin (admin.ModelAdmin):
    inlines = (InscripcionInLine,)
