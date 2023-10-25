import os
import shutil

def criar_diretorio_projeto(projeto,diretorio_base):

    diretorio_treino = os.path.join(diretorio_base, 'treino')
    diretorio_teste = os.path.join(diretorio_base, 'teste')

    split_ratio = (projeto.treino) / 100

    if not os.path.exists(diretorio_base):
        os.makedirs(diretorio_base)

    if not os.path.exists(diretorio_treino):
        os.makedirs(diretorio_treino)
    if not os.path.exists(diretorio_teste):
        os.makedirs(diretorio_teste)


    for rotulo in projeto.rotulos.all():

        total_images = len(rotulo.imagensrotuladas.all())
        num_images_treino = int(total_images * split_ratio)
        

        diretorio_rotulo_treino = os.path.join(diretorio_treino, rotulo.nome)
        diretorio_rotulo_teste = os.path.join(diretorio_teste, rotulo.nome)
        if not os.path.exists(diretorio_rotulo_treino):
            os.makedirs(diretorio_rotulo_treino)

        if not os.path.exists(diretorio_rotulo_teste):
            os.makedirs(diretorio_rotulo_teste)

        for i, obj in enumerate(rotulo.imagensrotuladas.all()):
            source_image = obj.imagem.imagem.path 
            if i < num_images_treino:
                destination = os.path.join(diretorio_rotulo_treino, f"image_{i}.jpg")
            else:
                destination = os.path.join(diretorio_rotulo_teste, f"image_{i}.jpg")
            shutil.copy(source_image, destination)
    
