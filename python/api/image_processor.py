# pip install opencv-python

import cv2


# Visualizar  as imagens
def image_resizer(Ficheiro:str)->str:
    '''
    Ficheiro: é uma string que deve ser passada indicando 
    o caminho completo até a imagem em questão incluindo a extensão.
    Extensões suportadas: (png, jpeg, jpg, bmp)

    O código retorna a uma string com o novo tamanho da imagem (128,128,3)
    '''
    imagem = cv2.imread(Ficheiro)
    imagem=cv2.resize(imagem,(128,128), interpolation = cv2.INTER_AREA)

    return imagem.shape


print(image_resizer('NOME_DA_IMAGEM_.extensao'))
