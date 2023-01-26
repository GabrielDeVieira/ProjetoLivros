from django.db import models

# Create your models here.
class Livros(models.Model):
    liv_codigo = models.AutoField( primary_key=True,)
    liv_numerodepaginas = models.IntegerField(default=None)
    liv_nome = models.CharField(max_length=100)
    liv_dataleitura = models.DateField( null=True, blank=True)
    liv_autor = models.CharField(max_length=120)
    liv_avaliacao = models.TextField(null=True, blank=True)
    liv_leitura = models.BooleanField(default=False)
    def __str__ (self):
         return self.liv_nome