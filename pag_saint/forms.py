from django import forms
from django.forms import ValidationError
import re

##validaciones##
def no_numeros(value):
   if any(char.isdigit() for char in value):
      raise ValidationError (
         'El campo no permite numeros, %(valor)s',code='Ivalid',params={'valor': value})
   
def no_carateres_reg(value):
    re_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(re_email, value):
        raise ValidationError('Correo electrónico inválido')
    
def no_letras (value):
   if any(char.isalfa() for char in value):
      raise ValidationError ("No se permiten letras en este campo")

   
   
class ContactoForm ( forms.Form ):
    nombre = forms.CharField (
        label= "Nombre:", required = True, 
        validators= (no_numeros,),
        widget= forms.TextInput)
    
    apellido = forms.CharField (
        label= "Apellido:", required = True,
        validators= (no_numeros,),
        widget = forms.TextInput)
    
    email = forms.EmailField (      
        label= "Email:", required = True,
        validators= (no_carateres_reg,),
        widget= forms.EmailInput)
        
    mensaje = forms.CharField(
    label= "Mensaje:", required = False, widget=forms.Textarea)

    ##CLEANS##

    def clean_nombre(self):
       if self.cleaned_data["nombre"] == "odio":
         raise  ValidationError ("Palabra inapropiada")
       return self.cleaned_data["nombre"]

    def clean_apellido(self):
       if self.cleaned_data["apellido"] == "terror":
         raise  ValidationError ("Palabra inapropiada")
       return self.cleaned_data["apellido"]
    
    def clean_mensaje(self):
        mensaje=self.cleaned_data ['mensaje'] 
        if len(mensaje)<5:
            raise ValidationError(
                "Debes especificar mejor el mensaje que nos envias")
        return self.cleaned_data['mensaje']

    def clean(self):
      cleaned_data=super().clean()
      nombre= cleaned_data.get("nombre")
      apellido= cleaned_data.get("apellido")
      if nombre == "odio" and apellido == "terror":
         raise ValidationError("Palabra inapropiadas")
      return cleaned_data

