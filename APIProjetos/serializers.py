from rest_framework import serializers

from .models import Imagem, Rotulo, ImagemRotulada, Projeto


class ImagemSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Imagem
        fields = (
            'id',
            'usuario',
            'imagem',
            'criacao',

        )


class ImagemRotuladaSerializer(serializers.ModelSerializer):
    treino = serializers.BooleanField()
    imagem = serializers.HyperlinkedRelatedField( read_only=True,  view_name='imagem-detail')
    class Meta:
        model = ImagemRotulada
        fields = (
            'id',
            'usuario',
            'rotulo',
            'imagem',
            'criacao',
            'treino'
       
        )

#POR PADRAO DO DJANGO REST FRAMEWORK O NOME DA VIEW DE UMA INSTANCIA EH 'NOME_DO_MODELO-DETAIL'
class RotuloSerializer(serializers.ModelSerializer):
    imagensrotuladas = serializers.HyperlinkedRelatedField(many=True, read_only=True,  view_name='imagemrotulada-detail')
    class Meta:
        model = Rotulo
        fields = (
            'id',
            'usuario',
            'nome',
            'criacao',
            'imagensrotuladas'
            
         
        )


class ProjetoSerializer(serializers.ModelSerializer):

    rotulos= serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='rotulo-detail')
    class Meta:
        model = Projeto
        fields = (
            'id',
            'titulo',
            'usuario',
            'descricao',
            'criacao',
            'rotulos',
           
        )

