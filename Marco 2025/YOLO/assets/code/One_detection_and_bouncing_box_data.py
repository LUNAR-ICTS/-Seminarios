import cv2
from ultralytics import YOLO
import os

# Função para obter o nome do arquivo, extensão e diretório
def get_filename_and_extension(image_path):
    directory = os.path.dirname(image_path)
    filename, extension = os.path.splitext(os.path.basename(image_path))
    return filename, extension, directory + "\\"

# Inicializa o modelo YOLO
model = YOLO("yolo11m.pt")

# Exibe todas as classes disponíveis no modelo
'''print("Classes disponíveis no modelo YOLO:")
for class_id, label in model.names.items():
    print(f"ID: {class_id}, Label: {label}")'''

# Caminho da imagem a ser processada
image_path = r"Marco 2025\YOLO\assets\img\cats\image0.jpg"  # Substitua pelo caminho da imagem

# Lê a imagem
img = cv2.imread(image_path)

# Processa a imagem com o modelo YOLO
results = model(img)

# Lista para armazenar os resultados extraídos
detections = []

# Percorre os resultados
for result in results:
    boxes = result.boxes.xywh  # Coordenadas (x, y, largura, altura)
    confs = result.boxes.conf  # Confiança das detecções
    cls = result.boxes.cls  # Classes detectadas
    
    for i in range(len(boxes)):
        x_center, y_center, width, height = map(int, boxes[i])  # Converte para inteiros
        class_id = int(cls[i])  # Obtém a classe detectada
        confidence = float(confs[i])  # Confiança da detecção
        
        # Definir valores para classes específicas
        c14 = 1 if class_id == 14 else 0  # Classe Pássaro
        c15 = 1 if class_id == 15 else 0  # Classe Gato
        c16 = 1 if class_id == 16 else 0  # Classe Cachorro
        
        # Criar dicionário com os dados
        detection = {
            "Pc": confidence,
            "bx": x_center,
            "by": y_center,
            "bw": width,
            "bh": height,
            "c14": c14,
            "c15": c15,
            "c16": c16
        }
        detections.append(detection)

# Print dos resultados
for i, det in enumerate(detections):
    print(f"Detecção {i + 1}: {det}")
