import cv2
import numpy as np
import os

def extract_rgb_channels(image_path):
    # Carregar a imagem
    image = cv2.imread(image_path)
    if image is None:
        print("Erro ao carregar a imagem.")
        return
    
    # Separar os canais BGR (OpenCV usa BGR por padrão)
    B, G, R = cv2.split(image)
    
    # Criar imagens vazias para cada canal isolado
    zero_channel = np.zeros_like(B)
    
    # Criar imagens RGB separadas
    red_image = cv2.merge([zero_channel, zero_channel, R])
    green_image = cv2.merge([zero_channel, G, zero_channel])
    blue_image = cv2.merge([B, zero_channel, zero_channel])
    
    # Exibir as imagens
    cv2.imshow("Original", image)
    cv2.imshow("Red Channel", red_image)
    cv2.imshow("Green Channel", green_image)
    cv2.imshow("Blue Channel", blue_image)
    
    # Salvar as imagens
    cv2.imwrite("red_channel.png", red_image)
    cv2.imwrite("green_channel.png", green_image)
    cv2.imwrite("blue_channel.png", blue_image)
    
    # Aguardar tecla para fechar
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def get_filename_and_extension(image_path):
    filename, extension = os.path.splitext(os.path.basename(image_path))
    return filename, extension

# Exemplo de uso
image_path = r"Março 2025/YOLO/assets/img/Creeper_mine_painting.png"  # Substitua pelo caminho da sua imagem
extract_rgb_channels(image_path)
name, ext = get_filename_and_extension(image_path)
print(f"Nome do arquivo: {name}, Extensão: {ext}")
