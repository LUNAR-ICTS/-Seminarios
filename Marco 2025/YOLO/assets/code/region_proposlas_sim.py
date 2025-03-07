import cv2
import numpy as np
import random

def region_proposals_segmentation(image_path, output_path, num_regions=100):
    # Carrega a imagem
    img = cv2.imread(image_path)
    if img is None:
        print("Erro ao carregar a imagem.")
        return

    # Inicializa o Selective Search
    ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
    ss.setBaseImage(img)
    ss.switchToSelectiveSearchFast()  # Versão rápida para desempenho

    # Obtém as regiões propostas
    rects = ss.process()

    # Seleciona um subconjunto de regiões para exibição
    selected_regions = random.sample(list(rects), min(num_regions, len(rects)))

    # Cria uma máscara para a segmentação
    mask = np.zeros_like(img, dtype=np.uint8)

    # Gera cores aleatórias para cada região
    for (x, y, w, h) in selected_regions:
        color = [random.randint(50, 255) for _ in range(3)]  # Gera uma cor aleatória
        mask[y:y+h, x:x+w] = color  # Preenche a região na máscara

    # Combina a máscara com a imagem original
    segmented_img = cv2.addWeighted(img, 0.5, mask, 0.5, 0)

    # Salva e exibe a imagem segmentada
    cv2.imwrite(output_path, segmented_img)
    cv2.imshow("Region Proposals - Segmentação", segmented_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Exemplo de uso
image_path = r"D:\Academico\Liga\-Seminarios\Marco 2025\YOLO\assets\img\cats\image5.jpg"
output_path = r"D:\Academico\Liga\-Seminarios\Marco 2025\YOLO\assets\img\cats\image5_R_CNN_segmented.jpg"

region_proposals_segmentation(image_path, output_path, num_regions=50)
