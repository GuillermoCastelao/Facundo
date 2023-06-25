from django.db import models

class Alumnos(models.Model):
    idalum = models.BigAutoField(db_column='IdAlum', primary_key=True)
    idc = models.BigIntegerField(db_column='IdC', blank=True, null=True) 
    legajonro = models.BigIntegerField(db_column='LegajoNro', blank=True, null=True, verbose_name='Legajo') 
    cohorte = models.BigIntegerField(db_column='Cohorte', blank=True, null=True)
    apynom = models.CharField(db_column='ApyNom', max_length=255, blank=True, null=True,verbose_name='Estudiante')
    dni = models.CharField(db_column='DNI', max_length=255, blank=True, null=True, verbose_name='DNI')
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True, verbose_name='Correo')
    nacfecha = models.DateField(db_column='NacFecha', blank=True, null=True, verbose_name='Nacimiento') 

    class Meta:
        managed = False
        db_table = 'alumnos'
        
    def __str__(self):
        fila = "Estudiante: " + self.apynom + "-" + "DNI: " + self.dni
        return fila
    