from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
import h5py
import matplotlib.pyplot as plt
import joblib
import numpy as np

model = joblib.load('./model/modelo1.joblib')
encoder = joblib.load('./model/labels1.joblib')


with h5py.File('./points/data.h5', 'r') as f:
    data = f['data'][:]
    labels = f['labels'][:]
# Prepare the data
data = np.asarray(data)
labels = np.asarray(labels)
# print(labels)


#split the data
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True)

# print(y_test) #acá es binario [b'p' b'x' b'o' ... b'j' b'i' b'u']

# Decode byte-encoded labels to strings 
y_test = [label.decode('utf-8') if isinstance(label, bytes) else label for label in y_test]
# print(y_test) # acá son strings 'p', 'x', 'o', 'f', 'l', 'x', 'r', 'l',...

# Initialize the MultiLabelBinarizer
all_classes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'space', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Inicializar MultiLabelBinarizer con todas las clases
mlb = MultiLabelBinarizer(classes=all_classes)
y_test_binarized = mlb.fit_transform(y_test) #hot encode
# print("aca:",y_test_binarized) 

# Binarize the y_test labels
classes = mlb.classes_
  # print("Clases detectadas por MultiLabelBinarizer:", classes,type(classes))
# Predecir etiquetas para x_test
y_pred = model.predict(x_test)
print("letras verdaderas:", y_test[20:40])
print("indices predichos por el modelo:", y_pred[20:40])

# Convertir índices predichos a etiquetas reales usando las clases del MultiLabelBinarizer
y_pred_decoded = [classes[idx] for idx in y_pred]


# Obtener la matriz de confusión
cm = confusion_matrix(y_test, y_pred_decoded, labels=classes)

# Visualizar la matriz de confusión con etiquetas de clase
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classes)
disp.plot(cmap=plt.cm.Blues, xticks_rotation='vertical')
plt.title('Matriz de Confusión')
plt.show()
print("Etiquetas verdaderas (y_test):", y_test[:10])  # Muestra las primeras 10 etiquetas verdaderas
print("Etiquetas predichas (y_pred):", y_pred_decoded[:10])  # Muestra las primeras 10 predicciones
