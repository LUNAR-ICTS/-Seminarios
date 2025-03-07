import cv2
import numpy as np

def load_image(img_path):
    """Carrega a imagem e retorna a imagem e suas dimensões."""
    image = cv2.imread(img_path)
    if image is None:
        raise ValueError(f"Imagem não encontrada: {img_path}")
    return image, image.shape[:2]  # Retorna a imagem e suas dimensões (altura, largura)

def calculate_window_size(img_width, img_height, ratio=1/6):
    """Calcula o tamanho da janela deslizante com base na razão da imagem."""
    window_width = int(img_width * ratio)
    window_height = int(img_height * ratio)
    return (window_width, window_height)

def generate_sliding_window_frames(image, window_size):
    """Gera os frames percorrendo toda a imagem, garantindo que a janela não ultrapasse os limites."""
    img_height, img_width = image.shape[:2]
    frames = []
    step_size = window_size[0]  # Step igual ao tamanho da janela

    for y in range(0, img_height, step_size):
        for x in range(0, img_width, step_size):
            frame = image.copy()

            # Ajusta para que a janela nunca ultrapasse os limites da imagem
            x_start = min(x, img_width - window_size[0])
            y_start = min(y, img_height - window_size[1])
            x_end = x_start + window_size[0]
            y_end = y_start + window_size[1]

            # Desenha a janela ajustada
            cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (0, 0, 255), 8)
            frames.append(frame)

            # Se a janela já atingiu a borda direita, encerra o loop na horizontal
            if x_end >= img_width:
                break

        # Se a janela já atingiu a borda inferior, encerra o loop na vertical
        if y_end >= img_height:
            break

    return frames  # Retorna os quadros gerados

def create_video(frames, output_path, img_size, fps, duration):
    """Cria o vídeo ajustando a duração para que a sliding window percorra toda a imagem."""
    total_frames = fps * duration  # Total de frames que o vídeo deve ter
    num_frames = len(frames)

    if num_frames < total_frames:
        # Interpolar os frames para preencher o tempo total
        factor = total_frames // num_frames
        final_frames = []
        for frame in frames:
            final_frames.extend([frame] * factor)  # Repete cada frame para aumentar a duração
        final_frames = final_frames[:total_frames]  # Garante o número exato de frames
    else:
        final_frames = frames[:total_frames]  # Se houver mais frames que o necessário, corta a lista

    # Criar o vídeo
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video = cv2.VideoWriter(output_path, fourcc, fps, img_size)

    for frame in final_frames:
        video.write(frame)

    video.release()
    print(f"Vídeo salvo como {output_path}")

# Parâmetros
IMG_PATH = "Marco 2025\YOLO\assets\img\cats\image5.jpg"  # Substitua pelo caminho da sua imagem
WINDOW_RATIO = 1/4  # Janela será 1/6 do tamanho da imagem
FPS = 20
DURATION = 4  # Tempo do vídeo (em segundos)
OUTPUT_VIDEO = "Marco 2025\YOLO\assets\img\sliding_window3.mp4"

# Pipeline de execução
image, (img_height, img_width) = load_image(IMG_PATH)
window_size = calculate_window_size(img_width, img_height, WINDOW_RATIO)
frames = generate_sliding_window_frames(image, window_size)
create_video(frames, OUTPUT_VIDEO, (img_width, img_height), FPS, DURATION)
