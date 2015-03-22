from django.contrib import admin
from aula.models import Alumno
from aula.models import Clase
from aula.models import Ranking

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre'] 
    search_fields = ['nombre']

class ClaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre'] 
    search_fields = ['nombre']

class RankingAdmin(admin.ModelAdmin):
    search_fields = ['alumno__nombre', 'clase__nombre']

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Clase, ClaseAdmin)
admin.site.register(Ranking, RankingAdmin)
