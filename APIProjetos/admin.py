from django.contrib import admin

from .models import Imagem, ImagemRotulada, Projeto , Rotulo


@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
    list_display = ('id','imagem','criacao',)


@admin.register(ImagemRotulada)
class ImagemRotuladaAdmin(admin.ModelAdmin):
    list_display= ('id','rotulo','imagem','criacao' )

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display= ( 'id','titulo','usuario','descricao','criacao','rotulos',)


@admin.register(Rotulo)
class ImagemRotuladaAdmin(admin.ModelAdmin):
    list_display= ('id','nome','criacao' )