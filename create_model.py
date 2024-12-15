
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import h5py
import joblib
from sklearn.preprocessing import LabelEncoder

with h5py.File('./points/data.h5', 'r') as f:
    data = f['data'][:]
    labels = f['labels'][:]

data = np.asarray(data)
labels = np.asarray(labels)

encoder = LabelEncoder()
labels = encoder.fit_transform(labels)

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

model = RandomForestClassifier()

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)

print(f'{score * 100}% de Prediccion Correcta !')

joblib.dump(model, './model/modelo.joblib')
joblib.dump(encoder, './model/labels.joblib')