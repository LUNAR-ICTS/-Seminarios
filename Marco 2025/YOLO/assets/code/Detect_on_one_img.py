import cv2
from ultralytics import YOLO
import os

# Função para obter o nome do arquivo, extensão e diretório
def get_filename_and_extension(image_path):
    directory = os.path.dirname(image_path)
    filename, extension = os.path.splitext(os.path.basename(image_path))
    return filename, extension, directory + "\\"

# Inicializa o modelo YOLO
model = YOLO("yolo11x.pt")

# Caminho da imagem a ser processada
image_path = r"Marco 2025\YOLO\assets\img\cats\image7.jpg"  # Substitua pelo caminho da imagem

# Obtém o nome do arquivo, extensão e diretório
filename, extension, directory = get_filename_and_extension(image_path)
print(f"Nome do arquivo: {filename}\nExtensão: {extension}\nDiretório: {directory}")

# Lê a imagem
img = cv2.imread(image_path)

# Verifica se a imagem foi carregada corretamente
if img is None:
    print("Erro: Não foi possível carregar a imagem.")
    exit()

# Processa a imagem com o modelo YOLO
results = model(img)

# Copia a imagem original para desenhar as detecções
annotated_img = img.copy()

# Percorre os resultados
for result in results:
    # Obtém as detecções
    boxes = result.boxes.xyxy  # Coordenadas das bounding boxes
    confs = result.boxes.conf  # Confiança das detecções
    cls = result.boxes.cls  # Classes detectadas
    
    for i in range(len(boxes)):
        x1, y1, x2, y2 = map(int, boxes[i])  # Converte para inteiros
        label = f"{model.names[int(cls[i])]} {confs[i]:.2f}"  # Nome da classe e confiança

        # Desenha a bounding box com espessura maior
        cv2.rectangle(annotated_img, (x1, y1), (x2, y2), (0, 0, 255), thickness=15)

        # Adiciona a label com fonte maior
        font_scale = 2.0
        font_thickness = 6
        (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)
        cv2.rectangle(annotated_img, (x1, y1 - h - 5), (x1 + w, y1), (0, 0, 255), -1)  # Fundo da label
        cv2.putText(annotated_img, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), font_thickness)

# Salva a imagem com as detecções
output_path = f"{directory}{filename}_detect{extension}"
cv2.imwrite(output_path, annotated_img)
print(f"Imagem salva com sucesso em: {output_path}")

# Exibe a imagem com as detecções
cv2.imshow("Detecções", annotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
