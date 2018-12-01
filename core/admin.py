from django.contrib import admin
from .models import Region, Ciudad, Vivienda, Postulante, Raza, Estado, Mascotas

class PostulanteAdmin(admin .ModelAdmin):
    list_display = ('run', 'nombre' )
    search_fields = ['run']

admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Vivienda)
admin.site.register(Postulante, PostulanteAdmin)

class MascotasAdmin(admin.ModelAdmin):
    list_display = ('nombre','genero', 'raza','fecha_nacimiento','fecha_ingreso','estado')
    search_fields = ['nombre', 'fecha_ingreso']
    list_filter = ('fecha_ingreso',)


admin.site.register(Raza)
admin.site.register(Estado)
admin.site.register(Mascotas, MascotasAdmin)

