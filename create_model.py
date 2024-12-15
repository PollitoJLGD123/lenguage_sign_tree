
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import h5py
import joblib
import os
from sklearn.preprocessing import LabelEncoder

rutita = "./model"

with h5py.File('./points/data.h5', 'r') as f:
    data = f['data'][:]
    labels = f['labels'][:]

print(data)
print(labels)

data = np.asarray(data)
labels = np.asarray(labels)

print(data)
print(labels)

encoder = LabelEncoder()
labels = encoder.fit_transform(labels)

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

model = RandomForestClassifier()

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)

print(f'{score * 100}% de Prediccion Correcta !')

if not os.path.exists(rutita):
    os.makedirs(rutita)

joblib.dump(model, f'{rutita}/modelo.joblib')
joblib.dump(encoder, f'{rutita}/labels.joblib')