from django.db import models

### FORMULARIO DE CONTACTO ###

class Contacto (models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    email = models.CharField(max_length=50, verbose_name= "Email")
    mensaje = models.CharField(max_length=500, verbose_name="Mensaje")


### TABLAS DE PRODUCTOS ###

class Productos (models.Model):    
    codigo = models.CharField(max_length=30, primary_key=True)
    nombre = models.CharField(max_length=30)

"""

### BURGERS ###


class Burgers(models.Model):   
    nombre=models.CharField(max_length=30, verbose_name="Nombre")
    descripción=models.CharField(max_length=30, verbose_name="Descripción")
    produto=models.ForeignKey(Productos, null=False, blank=False, on_delete=models.CASCADE)

   


class Simples(Burgers):   
    cantidad= models.IntegerField(verbose_name="Cantidad")
    precio=models.IntegerField(verbose_name="Precio")
    produto=models.ForeignKey(Productos, null=False, blank=False, on_delete=models.CASCADE)
    
     


class Dobles(Burgers):   
    cantidad= models.IntegerField(verbose_name="Cantidad")
    precio=models.IntegerField(verbose_name="Precio")
    produto=models.ForeignKey(Productos, null=False, blank=False, on_delete=models.CASCADE)
    
  



### INDUMENTARIA ###

class Diseño(models.Model):    
    diseño_mano=models.CharField(max_length=30, verbose_name="Diseño Mano")
    diseño_cruz=models.CharField(max_length=30, verbose_name="Diseño Cruz")
    produto=models.ForeignKey(Productos, null=False, blank=False, on_delete=models.CASCADE)

    


class Talle(Diseño):     
    talle_S=models.CharField(max_length=30, verbose_name="S")
    talle_M=models.CharField(max_length=30, verbose_name="M")
    talle_L=models.CharField(max_length=30, verbose_name="L")
    talle_XL=models.CharField(max_length=30, verbose_name="XL")
    talle_XXL=models.CharField(max_length=30, verbose_name="XXL")
 
   

class Buzos(Talle):    
    buzos=models.CharField(max_length=30, verbose_name="Buzos")
    cantidad=models.CharField(max_length=30, verbose_name="Cantidad")
    produto=models.ForeignKey(Productos, null=False, blank=False, on_delete=models.CASCADE)

    #diseñoTalle=models.ManyToManyField(DiseñoTalle)  


class Remeras_mujer(Talle):   
    remera_M=models.CharField(max_length=30, verbose_name="Remeras Mujer")
    cantidad=models.CharField(max_length=30, verbose_name="Cantidad")
    produto=models.ForeignKey(Productos, null=False, blank=False, on_delete=models.CASCADE)

    #diseñoTalle=models.ManyToManyField(DiseñoTalle)



class Remeras_hombre(Talle):   
    remera_H=models.CharField(max_length=30, verbose_name="Remeras Hombrre")
    cantidad=models.CharField(max_length=30, verbose_name="Cantidad")
    produto=models.ForeignKey(Productos, null=False, blank=False, on_delete=models.CASCADE)
 

"""
 
 