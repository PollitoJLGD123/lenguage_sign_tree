El proyecto esta dedicado a la Inteligencia Artificial,
tiene la capacidad de entrenar un modelo que sea capaz de clasificar todas 
las letras del abecedario en señas, a través de la visión por computadora, usamos
un modelo de entrenamiento llamado Bosque Aleatorio (RandomForest) como modelo, 
el cual es un modelo dedicado a la clasificación de datos con diferentes salidas. 
El cual era perfecto para nuestro proyecto debido a la cantidad de letras
que posee nuestro abecedario. Se siguio 4 pasos, primero se hizo la recoleccion
de un dataset propio, el cual consisitia en tomar 200 fotos de nuestra mano para
cada letra del abecedario, todas estas fotos las guardamos en carpetas nombrando
cada una de estas con el nombre de la letra. Luego dentro de esas carpetas
recorrimos cada imagen y guardamos los puntos (Puntos extraídos de la libreria MEDIAPIPE)
dentro de un modelo basico con extension H5. Despues accedemos al archivo, utilizamos 
toda esta información almacenada para entrenar nuestro modelo de Bosque Aleatorio, 
dandonos asi un archivo totalmente entrenado con extensión Joblib. Por último utilizamos 
este modelo ya entrenado para la preodiccion y uso de lenguaje de señas. Obteniendo así una 
precisión de más del 90%.

1. Recaudar Imagenes
2. Recorrer Puntos
3. Create Model
4. Testing

Espero les sea de gran ayude y les guste mucho.
