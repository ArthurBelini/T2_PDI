import argparse
import cv2

import numpy as np

## Inicialização

# Tratamento da passagem de argumentos
parser = argparse.ArgumentParser(description='Filtragem High-Boost')
parser.add_argument('-k', '--kernel_size', type=int, default=5, help='Tamanho da matriz de convolucao (default: 5)')
args = parser.parse_args()
kernel_size = args.kernel_size

image_path = 'dipxe.tif'  # Caminho da imagem de entrada

## Passo 1: blur = conv(original)

original = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # imagem <- dados da imagem em tons de cinza

# Inicialização da matrix de convolucao (kernel)
kernel = np.ones((kernel_size, kernel_size), np.float32)
kernel /= kernel_size ** 2

blur = cv2.filter2D(original, -1, kernel)  # calcula imagem borrada

cv2.imwrite('blur.tif', blur)  # Salva imagem borrada











## Passo 2: mask = original - blur

















## Passo 3: new = original + w * mask 



# 320 x 138
