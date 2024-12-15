
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from mediapipe import solutions
import cv2
import numpy as np
import time

#from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

mediapipe_mano = solutions.hands
mediapipe_dibujito = solutions.drawing_utils
mediapipe_dibujo_estilo= solutions.drawing_styles
manos = mediapipe_mano.Hands(static_image_mode=True, min_detection_confidence=0.5, min_tracking_confidence=0.5)

labels = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
         "p","q","r","s","t","u","v","w","x","y","z","space"]


enabled = True

contar = 0
i = 0
lugar = "./dataset/train"

while True:
    ret, frame = cap.read()

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    resultado = manos.process(frame_rgb)

    frame_save = np.copy(frame)

    try:
        if resultado.multi_hand_landmarks:  # primero preguntamos si detecto una mano :)
            # ahora dentro del video vamos a detectar todos los puntos
            for mano_puntos in resultado.multi_hand_landmarks:

                x_min, y_min = float('inf'), float('inf')
                x_max, y_max = float('-inf'), float('-inf')
                for punto in mano_puntos.landmark:
                    x, y = int(punto.x * frame.shape[1]), int(punto.y * frame.shape[0])
                    if x < x_min:
                        x_min = x
                    if y < y_min:
                        y_min = y
                    if x > x_max:
                        x_max = x
                    if y > y_max:
                        y_max = y

                margen = int(0.05 * frame.shape[1])
                x_min = max(x_min - margen, 0)
                y_min = max(y_min - margen, 0)
                x_max = min(x_max + margen, frame.shape[1])
                y_max = min(y_max + margen, frame.shape[0])

                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
                mediapipe_dibujito.draw_landmarks(frame, mano_puntos, mediapipe_mano.HAND_CONNECTIONS,
                                                  mediapipe_dibujo_estilo.get_default_hand_landmarks_style(),
                                                  mediapipe_dibujo_estilo.get_default_hand_connections_style())
                img_blanca = frame[y_min:y_max, x_min:x_max]

                if enabled:
                    if cv2.waitKey(1) == ord('s'):
                        contar += 1
                        ruta = f"{lugar}/{labels[i]}"
                        if not os.path.exists(ruta):
                            os.makedirs(ruta)
                        cv2.imwrite(f"{ruta}/Imagen{time.time()}.jpg",frame_save)
                        print(f"Imagen {contar} letra {labels[i]}")

                    if contar == 200:
                        print(f"Se han guardado las 200 imágenes de la letra {labels[i]}")
                        i = i + 1
                        contar = 0
                        enabled = False

                    cv2.putText(frame, f"Letra: {labels[i]}", (10, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                    cv2.putText(frame, f"Cantidad Total: {contar}/{200}", (10, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                else:
                    cv2.putText(frame, f"Letra: {labels[i - 1]} terminada", (10, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                    cv2.putText(frame, f"Seguir presiona 'T'", (10, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

                    if cv2.waitKey(1) & 0xFF == ord('t'):
                        enabled = True

                cv2.imshow("Imagen Blanca", img_blanca)
    except:
        pass

    cv2.imshow("frame", frame)
    if cv2.waitKey(25) == ord('q') or i == len(labels):
        print(f"Se guardo todo, terminando")
        break

cv2.destroyAllWindows()
cap.release()

