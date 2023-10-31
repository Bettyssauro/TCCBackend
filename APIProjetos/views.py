from rest_framework import viewsets,status
from rest_framework.decorators import action

from rest_framework.response import Response
from django.http import HttpResponse

from .models import Imagem, ImagemRotulada, Projeto, Rotulo, User
from .serializers import ImagemSerializer, ImagemRotuladaSerializer, ProjetoSerializer, RotuloSerializer
from .diretorios_manager import criar_diretorio_projeto

import os
import zipfile
import re

class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer
    #RECEBE A IMAGEM CONTENT-TYPE MULTIPART/FORMDATA
    #RETORNA A IMAGEM RECEM CRIADA
    def create(self, request, *args, **kwargs):
        usuario = request.user
        imagem = Imagem(usuario=usuario,imagem=request.data['imagem'])
        imagem.save()
        serializer = ImagemSerializer(imagem)
        return Response(serializer.data)


class ImagemRotuladaViewSet(viewsets.ModelViewSet):
    queryset = ImagemRotulada.objects.all()
    serializer_class = ImagemRotuladaSerializer
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)  
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    
    #RECEBE SOMENTE OS IDS DE ROTULO E IMAGEM
    #RETORNA A IMAGEM ROTULADA Q FOI SALVA
    def create(self, request, *args, **kwargs):
        usuario = request.user
        rotulo_id = request.data.get('rotulo')
        imagem_id = request.data.get('imagem')

        try:
            rotulo = Rotulo.objects.get(id=rotulo_id)
            imagem = Imagem.objects.get(id=imagem_id)
        except Rotulo.DoesNotExist:
            return Response({'rotulo': ['Rótulo não encontrado.']}, status=status.HTTP_400_BAD_REQUEST)
        except Imagem.DoesNotExist:
            return Response({'imagem': ['Imagem não encontrada.']}, status=status.HTTP_400_BAD_REQUEST)

        imagemr = ImagemRotulada(usuario=usuario, imagem=imagem, rotulo=rotulo)
        imagemr.save()

        serializer = ImagemRotuladaSerializer(imagemr, context={'request': request})
        return Response(serializer.data)
    

    #RETORNA AS IMAGENS ROTULADAS QUE RECEBERAM A MESMA IMAGEM (OU SEJA, UMA IMAGEM QUE POSSUI ROTULOS DIFERENTES)
    #EXEMPLO .../IMAGENSR/1/MESMASIMAGENS RETORNA AS IMAGENS ROTULADAS QUE DIVIDEM A MESMA IMAGEM COM A IMAGEM ROTULADA DE ID 1
    @action(detail=True, methods=['get'])
    def mesmasimagens(self, request, pk=None):
        imagemr = self.get_object()
        serializer= ImagemSerializer(imagemr.imagem.imagensrotuladas, many=True,context={'request': request})
        return Response(serializer.data)
    
    #RETORNA AS IMAGENS ROTULADAS QUE RECEBERAM O MESMO ROTULO (OU SEJA, UMA LISTA DE IMAGENS ROTULADAS COM O MESMO ROTULO)
    #EXEMPLO .../IMAGENSR/1/MESMOSROTULOS RETORNA AS IMAGENS ROTULADAS QUE DIVIDEM O MESMO ROTULO DA IMAGEM ROTULADA DE ID 1
    @action(detail=True, methods=['get'])
    def mesmosrotulos(self, request, pk=None):
        imagemr = self.get_object()
        serializer= ImagemSerializer(imagemr.rotulo.imagensrotuladas, many=True,context={'request': request})
        return Response(serializer.data)

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    def get_queryset(self):
        return Projeto.objects.filter(usuario=self.request.user)
    serializer_class = ProjetoSerializer
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)  
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    

    def create(self, request):
        caminho_atual = os.path.abspath(__file__)
        diretorio_pai = os.path.dirname(caminho_atual)
        diretorio_avo = os.path.dirname(diretorio_pai)
        nomedodiretorio= re.sub(r'[^a-zA-Z0-9]', '_', request.data['titulo'])
        diretorio_base = os.path.join(diretorio_avo, nomedodiretorio)   
        

        usuario = request.user

        print(request.data)
        if request.data.get('rotulos'):
            rotulo_ids = request.data.get('rotulos', [])
            try:

                
              
                rotulos = Rotulo.objects.filter(id__in=rotulo_ids)

                projeto = Projeto(usuario=usuario, titulo=request.data['titulo'], descricao=request.data['descricao'],endereco=diretorio_base)
                projeto.save()
              
                projeto.rotulos.set(rotulos)
             
                projeto.save()

                

                serializer = ProjetoSerializer(projeto,context={'request': request})
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
             
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            projeto = Projeto(usuario=usuario, titulo=request.data['titulo'], descricao=request.data['descricao'],endereco=diretorio_base)
            projeto.save()
            
            serializer = ProjetoSerializer(projeto,context={'request': request})
            return Response(serializer.data)
    
    #RETORNA OS ROTULOS DO PROJETO
    ##EXEMPLO .../PROJETOS/1/ROTULOS RETORNA OS ROTULOS UTILIZADOS NO PROJETO DE ID 1
    @action(detail=True, methods=['get'])
    def rotulos(self, request, pk=None):
        projeto = self.get_object()
        serializer= RotuloSerializer(projeto.rotulos.all(), many=True,context={'request': request})
        return Response(serializer.data)
    

    #RETORNA O ZIPFILE DO PROJETO
    ##EXEMPLO .../PROJETOS/1/DATASET RETORNA O PROJETO ORGANIZADO EM DIRETORIOS
    @action(detail=True, methods=['get'])
    def dataset(self, request, pk=None):
        instance = self.get_object()
        endereco = instance.endereco

        criar_diretorio_projeto(instance,endereco)
    
        if os.path.isdir(endereco):
       
            zip_filename = os.path.basename(endereco) + '.zip'
            with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(endereco):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, endereco)
                        zipf.write(file_path, arcname)

    
            response = HttpResponse(open(zip_filename, 'rb').read())
            response['Content-Type'] = 'application/zip'
            response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'

    
            os.remove(zip_filename)
        else:
            response = Response({"error": "Diretório não encontrado"}, status=404)

        return response

class RotuloViewSet(viewsets.ModelViewSet):
    queryset = Rotulo.objects.all()
    serializer_class = RotuloSerializer

    #RETORNA OS PROJETOS QUE UTILIZAM ESSE ROTULO
    #EXEMPLO .../ROTULOS/1/PROJETOS RETORNA TODOS OS PROJETOS QUE UTILIZAM O ROTULO DE ID 1
    @action(detail=True, methods=['get'])
    def projetos(self, request, pk=None):
        rotulo = self.get_object()
        serializer= ProjetoSerializer(rotulo.projetos.all(), many=True)
        return Response(serializer.data)
    
    #RETORNA AS IMAGENS ROTULADAS QUE POSSUEM ESSE ROTULO
    ##EXEMPLO: .../ROTULOS/1/IMAGENSROTULADAS RETORNA TODAS AS IMAGENS ROTULADAS COM O ROTULO DE ID 1
    @action(detail=True, methods=['get'])
    def imagensrotuladas(self, request, pk=None):
        rotulo = self.get_object()
        serializer= ImagemRotuladaSerializer(rotulo.imagensrotuladas.all(), many=True,context={'request': request})
        return Response(serializer.data)
    
    #RECEBE NOME DO ROTULO
    #RETORNA ROTULO Q FOI SALVO
    def create(self, request):
        usuario = request.user
        rotulo = Rotulo(usuario=usuario, nome=request.data['nome'])
        rotulo.save()
        serializer = RotuloSerializer(rotulo)
        return Response(serializer.data)