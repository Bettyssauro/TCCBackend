

#  UTILIZAR .VIEWS


# from rest_framework import generics

# from .models import Imagem, ImagemRotulada, Projeto, Rotulo
# from .serializers import ImagemSerializer, ImagemRotuladaSerializer, ProjetoSerializer, RotuloSerializer


# class ImagensAPIView(generics.ListCreateAPIView):
#     queryset = Imagem.objects.all()
#     serializer_class = ImagemSerializer   

# class ImagemAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Imagem.objects.all()
#     serializer_class = ImagemSerializer  

# class ImagemRotuladaAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ImagemRotulada.objects.all()
#     serializer_class = ImagemRotuladaSerializer 

# class ImagensRotuladasAPIView(generics.ListCreateAPIView):
#     queryset = ImagemRotulada.objects.all()
#     serializer_class = ImagemRotuladaSerializer

# class ProjetoAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Projeto.objects.all()
#     serializer_class = ProjetoSerializer


# class ProjetosAPIView(generics.ListCreateAPIView):
#     queryset = Projeto.objects.all()
#     serializer_class = ProjetoSerializer


# class RotuloAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rotulo.objects.all()
#     serializer_class = RotuloSerializer

# class RotulosAPIView(generics.ListCreateAPIView):
#     queryset = Rotulo.objects.all()
#     serializer_class = RotuloSerializer

#     def get_queryset(self):
#         if self.kwargs.get('projeto_pk'):

#             return self.queryset.filter(projetos=self.kwargs.get('projeto_pk'))
#         return self.queryset.all()

    