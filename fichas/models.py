from django.db import models


class Dueno(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.rut})"

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Dueño'
        verbose_name_plural = 'Dueños'


class Mascota(models.Model):
    nombre = models.CharField(max_length=80)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=80, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'


class ConsultaMedica(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=200)
    diagnostico = models.TextField()
    tratamiento = models.TextField(blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.mascota.nombre} - {self.motivo}"

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Consulta Médica'
        verbose_name_plural = 'Consultas Médicas'
# Create your models here.
