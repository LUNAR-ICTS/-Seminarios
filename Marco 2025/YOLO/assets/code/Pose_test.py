import cv2
from ultralytics import YOLO

def process_video(input_video_path, output_video_path, model_path="yolo11x-pose.pt"):
    # Carregar o modelo YOLO para detecção de poses
    model = YOLO(model_path)

    # Abrir o vídeo de entrada
    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        print("Erro ao abrir o vídeo de entrada.")
        return

    # Obter informações do vídeo
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para salvar o vídeo

    # Criar o vídeo de saída
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Aplicar YOLO para detecção de poses
        results = model(frame)

        # Renderizar as detecções na imagem
        annotated_frame = results[0].plot()

        # Escrever o frame no vídeo de saída
        out.write(annotated_frame)

        # Exibir o frame processado (opcional)
        cv2.imshow('YOLO Pose Detection', annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar recursos
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Vídeo processado salvo em: {output_video_path}")

# Exemplo de uso
input_video = r"Marco 2025\YOLO\assets\video\Rebeca.mp4"  # Substitua pelo caminho do seu vídeo de entrada
output_video = r"Marco 2025\YOLO\assets\video\Rebeca_poses.mp4"  # Nome do vídeo de saída
process_video(input_video, output_video)
