import cv2
import os
import numpy as np

def add_grid_to_image(image_path, num_squares_x=10, num_squares_y=10, color=(0, 255, 0), thickness=1):
    """
    Adiciona uma grade (grid) à imagem, dividindo-a em um número específico de quadrados.

    Parâmetros:
    - image_path: Caminho da imagem original.
    - num_squares_x: Número de quadrados na largura.
    - num_squares_y: Número de quadrados na altura.
    - color: Cor da grade no formato (B, G, R) (padrão: verde).
    - thickness: Espessura das linhas da grade (padrão: 1 pixel).
    """

    # Verifica se o arquivo existe
    if not os.path.exists(image_path):
        print("Erro: O arquivo da imagem não foi encontrado.")
        return

    # Lê a imagem
    img = cv2.imread(image_path)
    if img is None:
        print("Erro ao carregar a imagem.")
        return

    height, width, _ = img.shape  # Obtém dimensões da imagem

    # Calcula o tamanho dos quadrados
    square_width = width // num_squares_x
    square_height = height // num_squares_y

    # Desenha as linhas verticais e horizontais
    for i in range(1, num_squares_x):
        x = i * square_width
        cv2.line(img, (x, 0), (x, height), color, thickness)
    
    for j in range(1, num_squares_y):
        y = j * square_height
        cv2.line(img, (0, y), (width, y), color, thickness)

    # Obtém novo nome do arquivo
    directory, filename = os.path.split(image_path)
    name, ext = os.path.splitext(filename)
    new_filename = f"{name}_gridded{ext}"
    output_path = os.path.join(directory, new_filename)

    # Salva a nova imagem
    cv2.imwrite(output_path, img)
    print(f"Imagem salva com grid em: {output_path}")

    # Exibe a imagem processada
    cv2.imshow("Imagem com Grid", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Exemplo de uso
n = 3 # Número de quadrados
image_path = r"Marco 2025\YOLO\assets\img\cats\image7_detect.jpg"  # Substitua pelo caminho correto da sua imagem
add_grid_to_image(image_path, num_squares_x=n, num_squares_y=n, color=(0, 255, 0), thickness=2)
