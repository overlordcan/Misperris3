from django.urls import path
from .views import formulario_mascotas, listar_mascota, eliminar_mascota, modificar_mascota, crear_token
 
urlpatterns =[    
    path('formulario_mascota/', formulario_mascotas, name="api_formulario_mascota"),
    path('listar_mascota/', listar_mascota, name="api_listar_mascota"),
    path('eliminar-mascota/<id>/', eliminar_mascota, name="api_eliminar_mascota"),
    path('modificar_mascota/<id>/', modificar_mascota, name="api_modificar_mascota" ),
    path('crear-token/', crear_token, name="api_crear_token"), 
]