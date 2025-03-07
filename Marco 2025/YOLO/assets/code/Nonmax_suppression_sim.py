import cv2
import numpy as np

# Caminhos dos arquivos
image_path = r"Marco 2025\YOLO\assets\img\cats\image0.jpg"  # Imagem de entrada
output_path = r"Marco 2025\YOLO\assets\img\cats\image0_nom_max_sim.jpg"  # Caminho da imagem saída

# Carregar a imagem
img = cv2.imread(image_path)

# Verifica se a imagem foi carregada corretamente
if img is None:
    print("Erro: Não foi possível carregar a imagem.")
    exit()

# Bounding Box Principal (dados fornecidos)
best_box = {'Pc': 0.94, 'bx': 536, 'by': 551, 'bw': 530, 'bh': 896}

# Calcular as coordenadas da bounding box principal
best_x1 = best_box["bx"] - best_box["bw"] // 2
best_y1 = best_box["by"] - best_box["bh"] // 2
best_x2 = best_box["bx"] + best_box["bw"] // 2
best_y2 = best_box["by"] + best_box["bh"] // 2

# Simular bounding boxes levemente deslocadas e menores
bounding_boxes = [
    (best_x1 - 30, best_y1 - 30, best_x2 - 40, best_y2 - 40, 0.85),
    (best_x1 + 20, best_y1 + 15, best_x2 + 30, best_y2 + 25, 0.80),
    (best_x1 - 15, best_y1 - 10, best_x2 + 20, best_y2 + 15, 0.78),
    (best_x1 + 10, best_y1 + 10, best_x2 - 10, best_y2 - 10, 0.88)
]

# Função para desenhar bounding boxes
def draw_bounding_box(img, x1, y1, x2, y2, conf, color, thickness=5, text_offset=0):
    cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)
    label = f"cat {conf:.2f}"
    
    # Adiciona um fundo para melhor leitura do texto
    (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 1, 3)
    cv2.rectangle(img, (x1, y1 - h - 10 + text_offset), (x1 + w, y1 + text_offset), color, -1)
    cv2.putText(img, label, (x1, y1 - 5 + text_offset),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

# Desenhar as bounding boxes **menos confiáveis** primeiro (em azul)
text_offsets = [0, 30, 60, 90]  # Evita sobreposição do texto
for i, box in enumerate(bounding_boxes):
    x1, y1, x2, y2, conf = box
    draw_bounding_box(img, x1, y1, x2, y2, conf, (255, 0, 0), 5, text_offsets[i])

# **Desenhar a bounding box principal por último em vermelho**
draw_bounding_box(img, best_x1, best_y1, best_x2, best_y2, best_box['Pc'], (0, 0, 255), 8)

# Salvar a imagem processada
cv2.imwrite(output_path, img)
print(f"Imagem salva com sucesso em: {output_path}")

# Exibir a imagem
cv2.imshow("Non-Max Suppression Simulation", img)
cv2.waitKey(0)
cv2.destroyAllWindows()