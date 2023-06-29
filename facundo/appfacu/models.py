from django.db import models

class Usuarios(models.Model):
    iduser = models.BigAutoField(db_column='IdUser', primary_key=True)
    usuario = models.CharField(db_column='Usuario', max_length=255, blank=True, null=True)  
    clave = models.CharField(db_column='Clave', max_length=255, blank=True, null=True)  
    perfil = models.CharField(db_column='Perfil', max_length=255, blank=True, null=True)  
    perfil2 = models.CharField(db_column='Perfil2', max_length=255, blank=True, null=True)  
    apeynom = models.CharField(db_column='ApeyNom', max_length=255, blank=True, null=True)  
    apellido = models.CharField(db_column='Apellido', max_length=255, blank=True, null=True)  
    nombres = models.CharField(db_column='Nombres', max_length=255, blank=True, null=True)  
    dni = models.CharField(db_column='DNI', max_length=255, blank=True, null=True)  
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  
    eq1 = models.CharField(db_column='EQ1', max_length=255, blank=True, null=True)  
    eq2 = models.CharField(db_column='EQ2', max_length=255, blank=True, null=True)  
    eq3 = models.CharField(db_column='EQ3', max_length=255, blank=True, null=True)  
    caduca = models.DateField(db_column='Caduca', blank=True, null=True)    

    class Meta:
        managed = False
        db_table = 'usuarios'

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
    