from django.db import models

# Create your models here.
class Detec(models.Model):
    Id_sensor = models.IntegerField()
    Estado_sensor = models.CharField(max_length=100)
    Municipio_sensor = models.CharField(max_length=100)
    Bairro_sensor = models.CharField(max_length=100)
    Deteccao_sensor = models.BooleanField()
    DataHora_sensor = models.DateTimeField()