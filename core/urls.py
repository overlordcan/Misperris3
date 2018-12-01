from django.urls import path
from .views import home, formulario, galeria, formulario_mascota, listar_mascota, eliminar_mascota, modificar_mascota
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('formulario/', formulario , name="formulario"),
    path('galeria/', galeria, name="galeria"),
    path('formulario_mascota/', formulario_mascota, name="formulario_mascota"),
    path('listar_mascota/', listar_mascota, name="listar_mascota"),
    path('eliminar-mascota/<id>/', eliminar_mascota, name="eliminar_mascota"),
    path('modificar_mascota/<id>/', modificar_mascota, name="modificar_mascota" )    
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)