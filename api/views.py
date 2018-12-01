from django.shortcuts import render

from django.core import serializers

from django.http import HttpResponse, HttpResponseBadRequest

import json

from core.models import Region, Ciudad, Postulante, Vivienda, Raza, Estado, Mascotas

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from fcm_django.models import FCMDevice

@csrf_exempt
@require_http_methods(['POST'])
def crear_token(request):

    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)
    token = bodyDict['token']

    existe = FCMDevice.objects.filter(registration_id=token, active=True)

    if existe:
        return HttpResponseBadRequest(json.dumps({'mensaje':'El token ya existe'}), content_type="application/json")

    

    dispositivo = FCMDevice()
    dispositivo. registration_id = token
    dispositivo.active = True
    
    if request.user.is_authenticated:
        dispositivo.user = request.user
    
    try:
        dispositivo.save()
        return HttpResponse(json.dumps({'mensaje':'Token guardado'}), content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'El token no ha podido ser almacenado'}), content_type="application/json")


# Create your views here.
def listar_mascota(request):
    mascota = Mascotas.objects.all()
    #transforamos el arreglo de autos a json
    mascotaJson = serializers.serialize('json', mascota)

    #devolvemos el json al usuario
    return HttpResponse(mascotaJson, content_type="application/json")

@csrf_exempt
@require_http_methods(['POST'])
def formulario_mascotas(request):
    body = request.body.decode('utf-8')
    #tranforma el body que esta en string a un diccionario de python
    bodyDict = json.loads(body)

    mascota = Mascotas()
    mascota.nombre = bodyDict['nombre']
    mascota.raza = Raza(id=bodyDict['raza_id'])
    mascota.genero = bodyDict['genero']
    mascota.fecha_ingreso = bodyDict['fecha_ingreso']
    mascota.fecha_nacimiento = bodyDict['fecha_nacimiento']
    mascota.descripcion = bodyDict['descripcion']
    mascota.estado = Estado(id=bodyDict['estado_id'])

    try:
        mascota.save()
        return HttpResponse(json.dumps({'mensaje':'Agregado correctamente'}), content_type="application/json")
    except:
        #retornaremos un mjensaje con un codigo de error
        return HttpResponseBadRequest(json.dumps({'mensaje':'Error al agregar'}), content_type="application/json")

@csrf_exempt
@require_http_methods(['PUT'])
def modificar_mascota(request):
    body = request.body.decode('utf-8')
    
    bodyDict = json.loads(body)

    mascota = Mascotas()
    mascota.id = bodyDict['id']
    mascota.nombre = bodyDict['nombre']
    mascota.raza = Raza(id=bodyDict['raza_id'])
    mascota.genero = bodyDict['genero']
    mascota.fecha_ingreso = bodyDict['fecha_ingreso']
    mascota.fecha_nacimiento = bodyDict['fecha_nacimiento']
    mascota.descripcion = bodyDict['descripcion']
    mascota.estado = Estado(id=bodyDict['estado_id'])

    try:
        mascota.save()
        return HttpResponse(json.dumps({'mensaje':'Modificado correctamente'}), content_type="application/json")
    except:
        #retornaremos un mjensaje con un codigo de error
        return HttpResponseBadRequest(json.dumps({'mensaje':'Error al modificar'}), content_type="application/json")

@csrf_exempt
@require_http_methods(['DELETE'])
def eliminar_mascota(request, id):
    try:
        mascota = Mascotas.objects.get(id=id)
        mascota.delete()
        return HttpResponse(json.dumps({'mensaje':'Eliminado correctamente'}), content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'Error al eliminar'}), content_type="application/json")