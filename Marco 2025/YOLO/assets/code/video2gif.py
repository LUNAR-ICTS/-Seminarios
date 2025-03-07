import cv2
import imageio
import os
import numpy as np

def video_to_gif(video_path, output_gif_prefix, fps=30, num_parts=3):
    # Verifica se o vídeo existe
    if not os.path.exists(video_path):
        print("Erro: O arquivo de vídeo não foi encontrado.")
        return
    
    # Captura o vídeo
    cap = cv2.VideoCapture(video_path)
    
    # Obtém a taxa de quadros e o número total de frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frames_per_part = total_frames // num_parts
    
    # Lista para armazenar os frames de cada parte
    all_frames = []
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Converte o frame para RGB (OpenCV lê em BGR)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Adiciona o frame à lista
        all_frames.append(frame)
    
    # Libera o vídeo
    cap.release()
    
    # Divide os frames em partes e salva os GIFs
    if all_frames:
        for i in range(num_parts):
            start_idx = i * frames_per_part
            end_idx = (i + 1) * frames_per_part if i < num_parts - 1 else len(all_frames)
            
            part_frames = all_frames[start_idx:end_idx]
            output_gif = f"{output_gif_prefix}_part{i+1}.gif"
            
            imageio.mimsave(output_gif, part_frames, fps=fps)
            print(f"GIF salvo com sucesso em: {output_gif}")
    else:
        print("Erro: Nenhum frame foi extraído do vídeo.")

# Exemplo de uso
video_path = r"Marco 2025\YOLO\assets\video\Output.mp4"  # Substitua pelo caminho do seu vídeo
output_gif_prefix = r"Marco 2025\YOLO\assets\img\video_seg"  # Prefixo dos GIFs

video_to_gif(video_path, output_gif_prefix, fps=30, num_parts=3)
