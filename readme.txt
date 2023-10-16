usage: script.py [-h] [-i IMAGE_PATH] [-c] [-n KERNEL_SIZE]
                 [-k WEIGHT] [-s SIGMA]

Filtragem High-Boost

options:
  -h, --help            show this help message and exit
  -i IMAGE_PATH, --image_path IMAGE_PATH
                        Caminho da imagem utilizada (default:      
                        dipxe.tif)
  -c, --use_conv        Utiliza convolucao como metodo de
                        borramento (default: False)
  -n KERNEL_SIZE, --kernel_size KERNEL_SIZE
                        Tamanho da matriz de convolucao (default:  
                        5)
  -k WEIGHT, --weight WEIGHT
                        Peso da filtragem high-boost ou k
                        (default: 4.5)
  -s SIGMA, --sigma SIGMA
                        Valor de sigma para borramento gaussiano   
                        (default: 3)

Exemplos:
  Exemplo do livro: gaussian blur, kernel size = 5, k = 4.5 e sigma = 3 
  > python script.py
  Utilizaco de convolucao: convolucao, kernel size = 5, k = 4.5 e sigma = 3 
  > python script.py -c