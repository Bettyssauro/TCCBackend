from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


##IMAGENS E IMAGENS ROTULADAS SAO CLASSES DIFERENTES
##A CLASSE DE IMAGENS ROTULADAS NA VERDADE SO REFERENCIA A UMA CLASSE IMAGEM E UM ROTULO
##DESSA FORMA UMA MESMA IMAGEM PODE ESTAR VINCULADA A DIFERENTES ROTULOS E UM ROTULO PODE ESTAR VINCULADO A VARIAS IMAGENS


#Classe base q todas as clases vao  herdar
class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        
class Imagem(Base):
    usuario = models.ForeignKey(User,related_name='imagenscriadas',on_delete=models.PROTECT)
    imagem = models.ImageField(upload_to='imagens/')

#antes do usuario ser deletado sera necessario apagar projeto por projeto  
class Projeto(Base):
    usuario = models.ForeignKey(User,related_name='projetos',on_delete=models.PROTECT)
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, default='')
    treino = models.DecimalField(max_digits=5, decimal_places=2, blank=True,default=70.0)
    teste = models.DecimalField(max_digits=5, decimal_places=2, blank=True,default=30.0)
    endereco = models.CharField(max_length=255,null=True, blank=True)
    

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        unique_together = ['usuario', 'titulo']
    def clean(self):
        if self.treino is not None and self.teste is not None:
            if self.treino + self.teste != 100:
                raise ValidationError("A soma de treino e teste deve ser igual a 100%.")
        elif (self.treino is not None and self.teste is None) or (self.treino is None and self.teste is not None):
            raise ValidationError("Ambos treino e teste devem estar preenchidos ou ambos vazios.")


    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

class Rotulo(Base):
    usuario = models.ForeignKey(User,related_name='rotulos',on_delete=models.PROTECT)
    nome = models.CharField(max_length=30,unique=True)
    projetos = models.ManyToManyField(Projeto,related_name='rotulos', blank=True)


class ImagemRotulada(Base):
    usuario = models.ForeignKey(User,related_name='imagensrotuladas',on_delete=models.PROTECT)
    rotulo = models.ForeignKey(Rotulo,related_name='imagensrotuladas',on_delete=models.CASCADE)
    imagem = models.ForeignKey(Imagem,related_name='imagensrotuladas',on_delete=models.CASCADE)
    treino = models.BooleanField(default=False)

    class Meta:
        unique_together = [ 'rotulo', 'imagem']

