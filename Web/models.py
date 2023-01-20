from django.db import models

# Create your models here.
class usuario(models.Model):
    idU = models.AutoField(auto_created=True,  primary_key=True, serialize=False, verbose_name='ID')
    nombreUser = models.CharField(max_length=40, null=True)
    apellidos = models.CharField(max_length=50, null=True)
    correo =  models.CharField(max_length=40, null=True)
    edad = models.PositiveIntegerField(null=True)
    usuario = models.CharField(max_length=30)
    password  = models.CharField(max_length=100)
    esAdmin = models.BooleanField()
    fechaCreacion = models.DateField()


class producto(models.Model):
    idP = models.AutoField(auto_created=True,  primary_key=True, serialize=False, verbose_name='ID')
    nombreProd =  models.CharField(max_length=40)
    versionProd = models.CharField(max_length=40)
    fechaCreacion =  models.DateField()
    fechaLimite = models.DateField()
    centroOrigen = models.CharField(max_length=700)
    productoRevisado = models.BooleanField()
    iteracion = models.IntegerField()


class listaVerificacion(models.Model):
    idLV = models.AutoField(auto_created=True,  primary_key=True, serialize=False, verbose_name='ID')
    nombreLV = models.CharField(max_length=200)
    fechaCreacion =  models.DateField()
    requisitoCalidad = models.CharField(max_length=100)





class preguntas(models.Model):
    idLV = models.ForeignKey(listaVerificacion,on_delete=models.CASCADE)
    idp = models.AutoField(auto_created=True,  primary_key=True, serialize=False, verbose_name='ID')
    
    No = models.IntegerField()
    preguta = models.CharField(max_length=2000)
    respuesta = models.CharField(max_length=50, null=True)
    observacion = models.CharField(max_length=1000, null=True)
    tipo = models.CharField(max_length=200)


class preguntasU(models.Model):
    idU = models.ForeignKey(usuario,on_delete=models.CASCADE)
    idLV = models.ForeignKey(listaVerificacion,on_delete=models.CASCADE)

    No = models.IntegerField()
    preguta = models.CharField(max_length=2000)
    respuesta = models.CharField(max_length=50, null=True)
    observacion = models.CharField(max_length=1000, null=True)
  
    modif = models.BooleanField()





class PUL(models.Model):
    idU = models.ForeignKey(usuario,on_delete=models.CASCADE)
    idLV = models.ForeignKey(listaVerificacion,on_delete=models.CASCADE)
    idP = models.ForeignKey(producto,on_delete=models.CASCADE)
    

