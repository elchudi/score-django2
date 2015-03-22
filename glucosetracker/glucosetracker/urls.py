from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import JsonResponse
from aula.models import Alumno
from aula.models import Clase
from aula.models import Ranking


def process_ranking(request):
    claseId = request.GET.get('clase')
    alumnoId =  request.GET.get('alumno')
    ranking = request.GET.get('ranking')
    alumno = Alumno.objects.get(id=int(alumnoId))
    clase = Clase.objects.get(id=int(claseId))
    to_save = Ranking(valor=int(ranking), alumno = alumno, clase= clase)
    to_save.save()
    return JsonResponse({'message':'ok'})

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scores.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^ranking/$', process_ranking),
)
