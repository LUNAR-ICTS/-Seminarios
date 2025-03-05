import cv2
import numpy as np
import os

def extract_matrix(image_path):
    # Carregar a imagem
    image = cv2.imread(image_path)
    if image is None:
        print("Erro ao carregar a imagem.")
        return
    
    print(f"Shape: {image.shape}")
    print("Channel R:")
    print(image[:, :, 2].tolist())
    print("Channel G:")
    print(image[:, :, 1].tolist())
    print("Channel B:")
    print(image[:, :, 0].tolist())

# Exemplo de uso
image_path = r"Marco 2025\YOLO\assets\img\Creeper_mine_painting_low_res.png"  # Substitua pelo caminho da sua imagem
extract_matrix(image_path)
