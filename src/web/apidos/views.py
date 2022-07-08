#from django.shortcuts import render, redirect, HttpResponse
import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
import json
# Create your views here.

class UsuarioView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# Método GET       
    def get(self, request, id=0):
        if (id>0):
            usuarios=list(Usuario.objects.filter(id=id).values())
            if len(usuarios)>0:
                usuario=usuarios[0]
                datos={'message':"Exito",'usuario':usuario}
            else:
                datos={'message':"Usuarios no encontrados..."}
            return JsonResponse(datos)
        else:
            usuarios=list(Usuario.objects.values())
            if len(usuarios)>0:
                datos={'message':"Exito",'usuarios':usuarios}
            else:
                datos={'message':"Usuarios no encontrados..."}
            return JsonResponse(datos)

# Método POST
    def post(self, request):
       # print (request.body)
        jd=json.loads(request.body)
       # print(jd)
        Usuario.objects.create(nombre=jd['nombre'],grupo=jd['grupo'],anno=jd['anno'])
        datos={'message':"Exito"}
        return JsonResponse(datos)

#Método PUT
    def put(self, request, id):
        jd=json.loads(request.body)
        usuarios=list(Usuario.objects.filter(id=id).values())
        if len(usuarios) > 0:
            usuario=Usuario.objects.get(id=id)
            usuario.nombre=jd['nombre']
            usuario.grupo=jd['grupo']
            usuario.anno=jd['anno']
            usuario.save()
            datos={'message':"Exito"}
        else:
            datos={'message':"Usuarios no encontrados..."}
        return JsonResponse(datos)

# Método DELETE
    def delete(self, request, id):
        usuarios=list(Usuario.objects.filter(id=id).values())
        if len(usuarios) > 0:
            Usuario.objects.filter(id=id).delete()
            datos={'message':"Exito"}
        else:
            datos={'message':"Usuarios no encontrados..."}
        return JsonResponse(datos)
        