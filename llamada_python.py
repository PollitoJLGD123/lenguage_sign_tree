import joblib
import cv2
import mediapipe as mp
import numpy as np
from audio_system import start_audio
import threading


model = joblib.load('./model/modelo.joblib')
encoder = joblib.load('./model/labels.joblib')

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

palabra = ""
seguir = True

say = ""

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.5)

while True:
    data_aux = []
    x_ = []
    y_ = []

    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

            for landmark in hand_landmarks.landmark:
                x_.append(landmark.x)
                y_.append(landmark.y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

            margen = 20
            x1 = max(0, int(min(x_) * w) - margen)
            y1 = max(0, int(min(y_) * h) - margen)
            x2 = min(w, int(max(x_) * w) + margen)
            y2 = min(h, int(max(y_) * h) + margen)

            prediction = model.predict([np.asarray(data_aux)])
            predicted_character = encoder.inverse_transform(prediction)[0].decode('utf-8')
            prediction_proba = model.predict_proba([np.asarray(data_aux)])
            confidence = prediction_proba.max() * 100

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)

            hand_frame = frame[y1:y2, x1:x2].copy()
            cv2.imshow('Mano Detectada', hand_frame)

            overlay = frame.copy()
            cv2.rectangle(frame, (x1, y1), (x2, y2), (100, 255, 0), 4)
            cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)

            bar_x1, bar_y1 = x1, y1 - 20
            bar_x2, bar_y2 = x1 + int((x2 - x1) * (confidence / 100)), y1 - 10
            cv2.rectangle(frame, (bar_x1, bar_y1), (bar_x2, bar_y2), (0, 255, 0), -1)
            cv2.putText(frame, f"{predicted_character} ({confidence:.2f}%)",
                        (x1 + 5, y1 - 30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (155, 155, 30), 2, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

