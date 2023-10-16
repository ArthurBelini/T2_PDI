import argparse
import cv2

import numpy as np


## Inicialização

# Tratamento da passagem de argumentos
n_default = 5
k_default = 4.5
s_default = 3
parser = argparse.ArgumentParser(description='Filtragem High-Boost')
parser.add_argument('-c', '--use_conv', action='store_true', default=False, help=f'Utiliza convolucao como metodo de borramento (default: False)')
parser.add_argument('-n', '--kernel_size', type=int, default=n_default, help=f'Tamanho da matriz de convolucao (default: {n_default})')
parser.add_argument('-k', '--weight', type=float, default=k_default, help=f'Peso da filtragem high-boost ou k (default: {k_default})')
parser.add_argument('-s', '--sigma', type=float, default=s_default, help=f'Valor de sigma para borramento gaussiano (default: {s_default})')
args = parser.parse_args()
use_conv = args.use_conv
kernel_size = args.kernel_size
weight = args.weight
sigma = args.sigma

image_path = 'dipxe.tif'  # Caminho da imagem de entrada


## Passo 1: blur = conv(original)

original = cv2.imread(image_path)  # imagem <- dados da imagem em tons de cinza

if kernel_size > 1:
    if use_conv:
        # Inicialização da matrix de convolucao (kernel)
        kernel = np.ones((kernel_size, kernel_size), np.float32)
        kernel /= kernel_size ** 2

        blur = cv2.filter2D(original, -1, kernel)  # blur <- convolucao de original
    elif kernel_size % 2 == 1:
        blur = cv2.GaussianBlur(original, (kernel_size, kernel_size), sigma)  # blur <- filtro gaussiano de original
    else:
        print('\'kernel_size\' deve ser impar para a utilizacao do filtro gaussiano')

        exit(1)
else:
    print('\'kernel_size\' deve ser maior que 1')

    exit(1)

cv2.imwrite('blur.tif', blur)  # Salva imagem borrada


## Passo 2: mask = original - blur

# Calcula diferenca entre original e borrada (mask)
mask = cv2.subtract(original, blur)

cv2.imwrite('mask.tif', mask)  # Salva diferenca entre original e borrada


## Passo 3: new = original + weight * mask 

# Calcula imagem com filtragem high-boost
new = cv2.multiply(mask, np.array([weight]))
new = cv2.add(original, new)
np.clip(new, 0, 255).astype(np.uint8)

cv2.imwrite('new.tif', new)  # Salva imagem com filtragem high-boost


## Mostrar imagens

cv2.imshow('Original Image', original)
cv2.imshow('Blurred Image', blur)
cv2.imshow('Difference Image', mask)
cv2.imshow('High-Boost Image', new)
cv2.waitKey(0)
cv2.destroyAllWindows()
