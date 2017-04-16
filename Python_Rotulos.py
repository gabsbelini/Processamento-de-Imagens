import cv2
import numpy as np

img = cv2.imread('baw3.png', 0)
matriz = np.asarray(img)
print(im)
cond = True
for idxLinha, linha in enumerate(matriz):
    idxColuna = 0
    for elem in linha:
        if elem == 255 and cond == True:
            x = idxLinha
            y = idxColuna
            print elem,  idxLinha, idxColuna
            cond = False
        idxColuna += 1
def verificaVizinhos(matriz, x, y ):
    lista = []
    if matriz[x-1][y-1] == 255:
        lista.append(x-1, y-1)
    if matriz[x-1][y] == 255:
        lista.append(x-1, y)
    if matriz[x+1][y] == 255:
        lista.append(x+1, y)
    if matriz[x+1][y+1]:
        lista.append(x+1, y+1)
    if matriz[x+1][y-1] == 255:
        lista.append(x+1, y-1)
    if matriz[x][y-1] == 255:
        lista.append(x, y-1)
    if matriz[x-1][y-1] == 255:
        lista.append(x-1, y-1)
    if matriz[x][y+1] == 255:
        lista.append(x, y+1)
    return lista



cv2.imshow('imagem', img)
cv2.waitKey(0)

