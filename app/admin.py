from django.contrib import admin
from app1.models import Editor,Autor,Libro

class EditorAdmin(admin.ModelAdmin):
    list_display= ('nombre','domicilio','ciudad','estado')
    search_fields=('nombre','domicilio','ciudad','estado')

class AutorAdmin(admin.ModelAdmin):
    list_display= ('nombre','apellido')
    search_fields=('nombre','apellido')


class LibroAdmin(admin.ModelAdmin):
    list_display= ('titulo','apellido','editor')
    search_fields=('titulo','autores__nombre','autores__apellido','editor__nombre')



# Register your models here.
admin.site.register(Editor,EditorAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Libro,LibroAdmin)