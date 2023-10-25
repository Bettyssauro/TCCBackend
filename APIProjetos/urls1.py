
#UTILIZAR .URLS
# COMPATIVEL COM .VIEWS2

# from django.urls import path

# from .views import ImagensAPIView, ImagemAPIView, ImagemRotuladaAPIView, ProjetoAPIView, RotuloAPIView, ImagensRotuladasAPIView, ProjetosAPIView, RotulosAPIView


# urlpatterns = [
#     path('imagens/', ImagensAPIView.as_view(), name='imagens'),
#     path('imagens/<int:pk>', ImagemAPIView.as_view(), name='imagens'),
#     path('imagensr/', ImagensRotuladasAPIView.as_view(), name='imagensr'),
#     path('imagensr/<int:pk>', ImagemRotuladaAPIView.as_view(), name='imagensr'),
    
#     path('projetos/', ProjetosAPIView.as_view(), name='projetos'),
#     path('projetos/<int:pk>', ProjetoAPIView.as_view(), name='projetos'),
#     path('projetos/<int:projeto_pk>/rotulos', RotulosAPIView.as_view(), name='projeto_rotulos'),

#     path('rotulos/', RotulosAPIView.as_view(), name='rotulos'),
#     path('rotulos/<int:pk>', RotuloAPIView.as_view(), name='rotulos'),
# ]