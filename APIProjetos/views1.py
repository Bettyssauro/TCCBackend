

# UTILIZAR .VIEWS

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from .models import Imagem, ImagemRotulada, Projeto, Rotulo
# from .serializers import ImagemSerializer, ImagemRotuladaSerializer, ProjetoSerializer, RotuloSerializer


# class ImagemAPIView(APIView):


#     def get(self, request):
#         imagens = Imagem.objects.all()
#         serializer = ImagemSerializer(imagens, many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = ImagemSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# class ImagemRotuladaAPIView(APIView):
    
#     def get(self, request):
#         imagens = ImagemRotulada.objects.all()
#         serializer = ImagemRotuladaSerializer(imagens, many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = ImagemRotuladaSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    


# class ProjetoAPIView(APIView):

#     def get(self, request):
#         projetos = Projeto.objects.all()
#         serializer = ProjetoSerializer(projetos, many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = ProjetoSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# class RotuloAPIView(APIView):

#     def get(self, request):
#         rotulos = Rotulo.objects.all()
#         serializer = RotuloSerializer(rotulos, many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = RotuloSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    