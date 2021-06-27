from django.db import models

class Categoria(models.Model):
    idCategoria= models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria= models.CharField(max_length=50, verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria

class registro_usuario(models.Model):
    username= models.CharField(max_length=20,primary_key=True, verbose_name='Username')
    mail= models.CharField(max_length=100,verbose_name='Correo')
    password= models.CharField(max_length=20, verbose_name='Password')

    def __str__(self):
        return self.username  
