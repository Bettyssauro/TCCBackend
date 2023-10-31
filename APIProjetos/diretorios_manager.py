import os
import shutil

def criar_diretorio_projeto(projeto, diretorio_base):
    

    diretorio_treino = os.path.join(diretorio_base, 'treino')
    diretorio_teste = os.path.join(diretorio_base, 'teste')

    if os.path.exists(diretorio_base):
        shutil.rmtree(diretorio_base)
    os.makedirs(diretorio_base)

    if not os.path.exists(diretorio_treino):
        os.makedirs(diretorio_treino)
    if not os.path.exists(diretorio_teste):
        os.makedirs(diretorio_teste)

    for rotulo in projeto.rotulos.all():
        diretorio_rotulo_treino = os.path.join(diretorio_treino, rotulo.nome)
        diretorio_rotulo_teste = os.path.join(diretorio_teste, rotulo.nome)

        if os.path.exists(diretorio_rotulo_treino):
            shutil.rmtree(diretorio_rotulo_treino)
        os.makedirs(diretorio_rotulo_treino)

        if os.path.exists(diretorio_rotulo_teste):
            shutil.rmtree(diretorio_rotulo_teste)
        os.makedirs(diretorio_rotulo_teste)

        for obj in rotulo.imagensrotuladas.all():
            source_image = obj.imagem.imagem.path
            if obj.treino == True:
                destination = os.path.join(diretorio_rotulo_treino, f"image_{obj.id}.jpg")
            else:
                destination = os.path.join(diretorio_rotulo_teste, f"image_{obj.id}.jpg")
            shutil.copy(source_image, destination)
