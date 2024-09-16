from django.contrib import admin
from .models import AuthorDB, FraseDB
# Register your models here.

admin.site.site_header = "¡Bienvenido!"
admin.site.index_title = "Administración de Frases y autores"

class FraseInLine(admin.TabularInline):
    model = FraseDB
    extra = 1
    
class AutAdmin(admin.ModelAdmin):
    fields = ['nombre',
              'fecha_nacimiento',
              'fecha_fallecimiento',
              'profesion',
              'nacionalidad']
    list_display = ['nombre', 'fecha_nacimiento']
    inlines = [FraseInLine]

    def actualizar_o(self, request, queryset):
        for obj in queryset:
            if "O" in obj.nombre:
                nombre1 = obj.nombre
                obj.nombre = nombre1.replace("O", "o")
                obj.save()
        
        self.message_user(request, "Letras O actualizadas")

    actualizar_o.short_description = "Actualizar letras O"

    actions = [actualizar_o]

admin.site.register(AuthorDB, AutAdmin)

@admin.register(FraseDB)
class FraseAdmin(admin.ModelAdmin):
    fields = ['cita', 'autor_fk']
    list_display = ['cita']