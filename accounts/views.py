from django.shortcuts import render

# Create your views here.

from .forms import CustomUserCreationForm

# Create your views here.

def register(request):

    variables = {                   #esto es para que el formulario llegue al template y poner la variable como tercer parametro en la linea de abajo
        'form': CustomUserCreationForm
    }

    #le pasamos al formulario de registro
    #todo lo que el usuario ingreso en el navegador
    if request.POST:
        form = CustomUserCreationForm(request.POST)
    #preguntaremos si el formulario es valido
        if form.is_valid():
            #si es valido le diremos que guarde los datos en BBDD
            form.save()
            variables['mensaje'] = "Usuario registrado!"
        else:
            variables['mensaje'] = "No se ha podido registrar el usuario"
            #si hay errores de validación debemos volver a enviar
            #el formulario al template ya que este lleva consigo
            #los mensajes de validacion
            variables['form'] = form

    return render(request, 'accounts/register.html',variables)

