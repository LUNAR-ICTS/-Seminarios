import cv2
import torch
from ultralytics import YOLO
import numpy as np

# Carregar modelo YOLOv8 para detecção de pose
model = YOLO("yolo11m-pose.pt")  # Certifique-se de que este é um modelo de pose

# Caminhos das imagens
input_image_path = r"Marco 2025\YOLO\assets\img\Morello.jpg"  # Substitua pelo caminho da sua imagem
output_image_path = r"Marco 2025\YOLO\assets\img\Morello_landmarks.jpg"  # Caminho para salvar a imagem processada

# Carregar a imagem
image = cv2.imread(input_image_path)

# Executar detecção
results = model(image)

# Processar os resultados
for result in results:
    if result.keypoints is not None:  # Verifica se há pontos detectados
        keypoints = result.keypoints.cpu().numpy()  # Converte para numpy se necessário
        
        for person in keypoints:  # Percorre todas as pessoas detectadas
            for kp in person:  # Cada ponto chave da pessoa
                if len(kp) >= 2:  # Certifica-se de que há pelo menos coordenadas x, y
                    x, y = int(kp[0]), int(kp[1])
                    cv2.circle(image, (x, y), 3, (0, 255, 0), -1)  # Desenha pontos

# Salvar a imagem processada
cv2.imwrite(output_image_path, image)

# Exibir a imagem processada
cv2.imshow("Landmarks Detectados", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Imagem salva em: {output_image_path}")
