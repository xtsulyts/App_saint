from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from  pag_saint.forms import ContactoForm
from django.urls import reverse
from django.contrib import messages
import sys
from pag_saint.models import Contacto
import os
      
# Create your views here.



def burgers (request):
    return render (request, "burgers.html")


def index (request):
    return render (request, "index.html")

def contacto(request, ):
  formulario = None
  if request.method == 'POST':
      
      formulario = ContactoForm ( request.POST )
      if formulario.is_valid ():
        messages.success(request, 'Recibimos tu mensaje')
             
        contacto_db = Contacto (
            nombre = formulario.cleaned_data ["nombre"],
            apellido = formulario.cleaned_data ["apellido"],
            email = formulario.cleaned_data ["email"],
            mensaje = formulario.cleaned_data ["mensaje"]
        )

        contacto_db.save()
        
        return redirect('index')

      else:
        messages.error(request, 'al cargar formulario')
       
  else:
      formulario = ContactoForm ()        
  context =  {
     'formulario_contacto'  : formulario 
    }
  return render(request, "contacto.html", context ) 


    

def reservas (request):
    return render (request, "reservas.html")



