from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ImagemViewSet, ImagemRotuladaViewSet, ProjetoViewSet, RotuloViewSet
router = SimpleRouter()
router.register('imagens', ImagemViewSet)
router.register('imagensr', ImagemRotuladaViewSet)
router.register('projetos', ProjetoViewSet)
router.register('rotulos', RotuloViewSet)
