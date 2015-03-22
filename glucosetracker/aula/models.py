from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=200, blank=False)
    def __repr__ (self):
        return '<Alumno %s>' % self.name

    def __str__ (self):
        return self.nombre

class Clase(models.Model):
    nombre = models.CharField(max_length=200, blank=False)
    alumnos = models.ManyToManyField(Alumno,  blank=True, verbose_name="Lista de alumnos")
    def __repr__ (self):
        return '<Clase %s>' % self.nombre

    def __str__ (self):
        return self.nombre

class Ranking(models.Model):
    valor = models.IntegerField()
    alumno = models.ForeignKey(Alumno)
    clase = models.ForeignKey(Clase)
     
    def __repr__ (self):
        return '<Alumno %s en clase %s: %s>' % self.alumno, self.clase, str(self.valor)

    def __str__ (self):
        #return '<Alumno %s en clase %s: %s>' % "a", "b", "C"
        return 'Alumno: %s. Clase: %s: Valor: %s' % (self.alumno, self.clase, str(self.valor))

