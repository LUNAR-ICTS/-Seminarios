import cv2
from ultralytics import YOLO
import os
import numpy as np

# Função para obter o nome do arquivo, extensão e diretório
def get_filename_and_extension(image_path):
    directory = os.path.dirname(image_path)
    filename, extension = os.path.splitext(os.path.basename(image_path))
    return filename, extension, directory + "\\"

# Inicializa o modelo YOLO para segmentação
model = YOLO("yolo11m-seg.pt")  # Certifique-se de usar um modelo treinado para segmentação

# Lê todos os arquivos da pasta "cats"
path = r"Marco 2025\YOLO\assets\img\cats\\"
files = os.listdir(path)

# Processa apenas imagens que não possuem "_detect" no nome
for file in files:
    if "_detect" in file or "_segm" in file:
        continue  # Pula arquivos já processados
    
    # Obtém o nome do arquivo, extensão e diretório
    filename, extension, directory = get_filename_and_extension(f"{path}{file}")
    print(f"Nome do arquivo: {filename}\nExtensão: {extension}\nDiretório: {directory}")
    
    # Lê a imagem
    img = cv2.imread(f"{directory}{filename}{extension}")
    
    # Processa a imagem com o modelo YOLO para segmentação
    results = model(img)

    # Copia a imagem original para desenhar as segmentações
    segmented_img = img.copy()

    # Percorre os resultados para cada imagem processada
    for result in results:
        # Obtém as máscaras de segmentação
        masks = result.masks.xy  # Coordenadas dos polígonos das máscaras
        cls = result.boxes.cls  # Classes detectadas
        
        overlay = segmented_img.copy()
        alpha = 0.3  # Transparência da segmentação

        for i, mask in enumerate(masks):
            # Converte as coordenadas para um formato adequado
            mask = mask.astype(int)
            
            # Preenche a área segmentada com uma cor vermelha transparente
            cv2.fillPoly(overlay, [mask], (0, 0, 255))
            
        # Aplica a transparência na segmentação
        segmented_img = cv2.addWeighted(overlay, alpha, segmented_img, 1 - alpha, 0)

    # Salva a imagem segmentada sem bounding boxes
    cv2.imwrite(f"{directory}{filename}_segm{extension}", segmented_img)

cv2.destroyAllWindows()
