import os
import pickle

import mediapipe as mp
import cv2
import h5py
import matplotlib.pyplot as plt


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

ruta_path = './dataset/train'

data = []
labels = []


for dir_ in os.listdir(ruta_path):
    for img_path in os.listdir(os.path.join(ruta_path, dir_)):
        data_aux = []

        x_ = []
        y_ = []

        img = cv2.imread(os.path.join(ruta_path, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            data.append(data_aux)
            labels.append(dir_)

h5_file = './points/data.h5'
with h5py.File(h5_file, 'w') as f:
    f.create_dataset('data', data=data)
    f.create_dataset('labels', data=labels)

print(f'Datos guardados en {h5_file}')

print("Datos para clasificacion de puntos (Mostrando 10 primeras listas):")
print(data[10])
print(labels[10])